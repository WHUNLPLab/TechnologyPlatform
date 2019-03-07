import json

from application.controller.base.base_service import BaseService
from application.models.graph.schema_models import EntityClass

class SchemaService(BaseService):

    def query_schema(self):
        records = EntityClass.query.all()

        # 梳理父子关系
        parent_childs = {}
        for record in records:
            parent_name = record.subClassOf.split(':')[1]
            name = record.prefLabel.split(':')[1]

            if parent_name not in parent_childs:
                parent_childs[parent_name] = []
            if name not in parent_childs:
                parent_childs[name] = []

            parent_childs[parent_name].append(record)


        schema_data = {
            'text': 'Thing',
            'tags': ['艺术垂域'],
            'nodes': [],
        }
        for child in parent_childs['Thing']:
            schema_data['nodes'].append(self.__represent_a_tree__(child, parent_childs))

        self.re_add_href(schema_data)
        return json.dumps([schema_data])
        return schema_data

    def query_a_entity_schema(self, entity_class):
        class_data = [
            {
                'label': 'CreativeWork(艺术作品)',
                'subPropertyOf': 'Thing',
                'domain': 'Person',
                'rangee': 'Thing',
                'comment': '备注',
                'functionalProperty': 'False',
                'symmetricProperty': 'False',
                'vertical': '艺术',
            },
            {
                'label': 'CreativeWork(艺术作品)',
                'subPropertyOf': 'Thing',
                'domain': 'Person',
                'rangee': 'Thing',
                'comment': '备注',
                'functionalProperty': 'False',
                'symmetricProperty': 'False',
                'vertical': '艺术',
            },
            {
                'label': 'CreativeWork(艺术作品)',
                'subPropertyOf': 'Thing',
                'domain': 'Person',
                'rangee': 'Thing',
                'comment': '备注',
                'functionalProperty': 'False',
                'symmetricProperty': 'False',
                'vertical': '艺术',
            },
        ]

        return class_data

    def __represent_a_tree__(self, root, nodes):
        """
        将以root为根节点的子树用dict表示
        Args:
            root: (string) 根节点
            nodes: (dict) 节点父子关系
        Return:
            dict表示的子树
        """

        name = root.prefLabel.split(':')[1]
        if len(nodes[name]) == 0:
            # 叶子节点
            data = {
                'text': name,
                'tags': [root.label],
            }
            return data
        else:
            data = {
                'text': name,
                'tags': [root.label],
                'nodes': [],
            }

            for child in nodes[name]:
                repr_child = self.__represent_a_tree__(child, nodes)
                data['nodes'].append(repr_child)

            return data

    def re_add_href(self, node):
        node['href'] = '/graph/schema/query?className=' + node['text']

        if 'nodes' not in node:
            return
        else:
            for child_node in node['nodes']:
                self.re_add_href(child_node)
