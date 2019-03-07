import os
import codecs
import datetime

from application import db
from application.models.tagger.models import Entity2Label

def request_a_entity(fromid=0):
    """
    获取一条待标注数据，展示给用户
    """

    try:
        entity2label = Entity2Label.query.filter(Entity2Label.text_id > fromid).filter_by(completed=False).first()
        labels = entity2label.label.split(',')

        json = {
            'title': entity2label.title,
            'text': entity2label.text,
            'labels': labels,
            'text_id': entity2label.text_id,
        }
        return True, json
    except Exception as e:
        return False, str(e)

def request_all_entity_labels():
    """
    获取所有实体类型标签信息
    """

    label_colors = ['#209CEE', '#009688', '#000000', '#FF3333', '#9933FF', '#F16728']
    labels = ['Person', 'Loc', 'Org', 'Work', 'Genre', 'Other']
    sequence_labels = ['PER', 'LOC', 'ORG', 'WOR', 'GEN', 'O']

    json = {'label_colors': label_colors,
            'labels': labels,
            'sequence_labels': sequence_labels,
            'label_num': 6}

    return json


def save_entity_label(text_id, labels, mark):
    """
    对用于标记的标签进行存储

    Args:
        text_id：标记的篇章索引
        labels：标记的标签
        mark：置信度
    Return:
        要进行关系标注的句子
    """
    concatenated_labels = ','.join(labels)
    entity2label = Entity2Label.query.get(text_id)

    relation_sentences = __sentence_fragment__(entity2label.text, labels)
    
    entity2label.label = concatenated_labels
    entity2label.mark = mark
    entity2label.completed = True
    entity2label.date = datetime.datetime.now()
    db.session.commit()

    return relation_sentences


def __sentence_fragment__(text, labels):
    """
    根据句号进行分句

    Args:
        text: (string) 整段文字
        labels: (list) 文字对应的标签
    Return:
        返回段落中每句话所对应的关系实例
    """

    sentences = text.strip().split('。')
    res = []

    sentence_start = 0
    for i, sentence in enumerate(sentences):
        if len(sentence) != 0:
            sentence_label = labels[sentence_start: (sentence_start + len(sentence))]
            entity_pars = __generate_entity_pair__(sentence, sentence_label)
            if entity_pars is not None:
                res.append(entity_pars)

        sentence_start += len(sentence) + 1

    return res


def __generate_entity_pair__(sentence, sentence_label):
    """
    在一句话中找出所有实体对

    Args:
        sentence: (string) 句子对应字符串
        sentence_label: (list) 句子对应实体标签
    Return:
        返回一句话中两两实体对构成的关系实例
    """

    # 预处理，加上句号，因此最后必然是‘O'类型
    sentence = sentence + '。'
    sentence_label.append('O')

    # 保存每个实体的类型信息和位置信息
    # (实体类型, 起始位置, 终止位置)
    entity_info = []

    for i, label in enumerate(sentence_label):
        if label[0] == 'B':
            entity_type = label[2:]
            entity_tuple = [entity_type, i, -1]
            entity_info.append(entity_tuple)
        elif label[0] == 'I' and sentence_label[i+1][0] == 'O':
            entity_info[-1][-1] = i

    if len(entity_info) < 2:
        return None

    # 两两组合成关系实例
    res = []
    for i in range(len(entity_info)):
        for j in range(len(entity_info)):
            if i != j:
                entity_head = entity_info[i]
                entity_tail = entity_info[j]
                head = sentence[entity_head[1] : entity_head[2]+1]
                tail = sentence[entity_tail[1] : entity_tail[2]+1]

                if entity_head[1] < entity_tail[1]:
                    relation_sentence = '{}<head>{}</head>{}<tail>{}</tail>{}'.format(
                        sentence[0 : entity_head[1]],
                        head,
                        sentence[entity_head[2]+1 : entity_tail[1]],
                        tail,
                        sentence[entity_tail[2]+1:]
                    )
                else:
                    relation_sentence = '{}<tail>{}</tail>{}<head>{}</head>{}'.format(
                        sentence[0 : entity_tail[1]],
                        tail,
                        sentence[entity_tail[2]+1 : entity_head[1]],
                        head,
                        sentence[entity_head[2]+1:]
                    )

                instance = {
                    'sentence': relation_sentence,
                    'head': head,
                    'tail': tail,
                    'head_type': entity_head[0],
                    'tail_type': entity_tail[0],
                }
                res.append(instance)

    return res
