"""
    处理关系标注的相关后台操作
"""

import datetime

from application import db
from application.models.tagger.models import Relation2Label

def request_a_relation(fromid):
    """
    请求一组数据用于标注
    """

    relation2label = Relation2Label.query.filter(Relation2Label.sentence_id > fromid).filter_by(completed=False).first()

    """
    sentence_id = 123
    sentence = '<head>齐白石</head>曾任中央美术学院名誉教授、中国美术家协会主席等职,代表作有《<tail>蛙声十里出山泉</tail>》《墨虾》等。著有《白石诗草》《白石老人自述》等。'
    head = '齐白石'
    tail = '蛙声十里出山泉'
    head_type = '人物(Person)'
    tail_type = '作品(Work)'
    relation_type = '未知关系(NA)' #该项若为空串，表示还未标记
    """

    json = {
        'sentence_id': relation2label.sentence_id,
        'sentence': relation2label.sentence,
        'head': relation2label.head,
        'tail': relation2label.tail,
        'head_type': relation2label.head_type,
        'tail_type': relation2label.tail_type,
        'relation_type': relation2label.relation_type,
    }

    return json


def request_all_relation_type(group_num=4):
    """
    请求所有的关系类型

    Args:
        group_num: 将所有类型分组，按组显示
    """

    relation_types = [
        {'relation_id': 0, 'relation_label': '/location/location/contains', 'relation_desc': '作品作者关系'},
        {'relation_id': 1, 'relation_label': '/location/location/contains', 'relation_desc': '位置包含关系'},
        {'relation_id': 2, 'relation_label': '/location/location/contains', 'relation_desc': '工作单位关系'},
        {'relation_id': 3, 'relation_label': '/location/location/contains', 'relation_desc': '出生位置关系'},
        {'relation_id': 4, 'relation_label': '/location/location/contains', 'relation_desc': '作品归属单位关系'},
        {'relation_id': 5, 'relation_label': '/location/location/contains', 'relation_desc': '作品艺术流派关系'},
        {'relation_id': 6, 'relation_label': '/location/location/contains', 'relation_desc': '配偶关系'},
        {'relation_id': 7, 'relation_label': '/location/location/contains', 'relation_desc': '父辈关系'},
        {'relation_id': 8, 'relation_label': '/location/location/contains', 'relation_desc': '兄弟关系'},
        {'relation_id': 9, 'relation_label': '/location/location/contains', 'relation_desc': '毕业院校关系'},
        {'relation_id': 10, 'relation_label': '/location/location/contains', 'relation_desc': '人物别名关系'},
        {'relation_id': 11, 'relation_label': '/location/location/contains', 'relation_desc': '作品创作地点关系'},
    ]

    json = []
    index = 0
    total = len(relation_types)
    for i in range(1, group_num+1, 1):
        num_one_col = int((total - i)/group_num) + 1
        types = relation_types[index: (index + num_one_col)]
        index += num_one_col
        json.append(types)

    return json


def save_relation_label(sentence_id, relation_id, mark):
    """
    用户标注完成后返回的数据

    Args:
        sentence_id: 标注的句子索引
        relation_id: 标注的关系类型
        mark: 用户对标注数据的置信度
    """

    relation2label = Relation2Label.query.get(sentence_id)
    relation2label.relation_type = relation_id
    relation2label.mark = mark
    relation2label.completed = True
    relation2label.date = datetime.datetime.now()

    db.session.commit()


def creat_relation_instances(instances):
    """
    进行了实体标注的文本将自动被要求标注关系

    Args:
        instances: (list) 若干个要标注关系的句子
    """

    for i, sentence in enumerate(instances):
        for instance in sentence:
            relation2label = Relation2Label()
            relation2label.sentence = instance['sentence']
            relation2label.head = instance['head']
            relation2label.tail = instance['tail']
            relation2label.head_type = instance['head_type']
            relation2label.tail_type = instance['tail_type']
            relation2label.relation_type = 0
            relation2label.completed = 0
            relation2label.date = datetime.datetime.now()
            relation2label.mark = 0

            db.session.add(relation2label)

    db.session.commit()
