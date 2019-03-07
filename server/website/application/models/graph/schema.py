# -*- coding:utf-8 -*-
import json


def get_schema():
    schema_data = {
        'text': 'Thing',
        'tags': ['2018-08-28'],
        'nodes': [
            {
                'text': 'Person',
                'tags': ['2018-08-28'],
                'nodes': [
                    {
                        'text': 'Artist',
                        'tags': ['2018-08-28'],
                    },
                    {
                        'text': 'Musician',
                        'tags': ['2018-08-28'],
                    },
                    {
                        'text': 'Drammatist',
                        'tags': ['2018-08-28'],
                    },
                    {
                        'text': 'Writer',
                        'tags': ['2018-08-28'],
                    }
                ]
            },
            {
                'text': 'CreativeWork',
                'tags': ['2018-08-28'],
                'nodes': [
                    {
                        'text': 'FineArtWork',
                        'tags': ['2018-08-28'],
                    },
                    {
                        'text': 'MusicWork',
                        'tags': ['2018-08-28'],
                    },
                ]
            },
            {
                'text': 'Location',
                'tags': ['2018-08-28'],
                'nodes': [
                    {
                        'text': 'ChineseLocation',
                        'tags': ['2018-08-28'],
                    }
                ]
            },
            {
                'text': 'Organization',
                'tags': ['2018-08-28'],
                'nodes': [
                    {
                        'text': 'EducationOrganization',
                        'tags': ['2018-08-28'],
                    },
                    {
                        'text': 'EntertainmentOrganization',
                        'tags': ['2018-08-28'],
                    },
                ]
            },
            {
                'text': 'Genre',
                'tags': ['2018-08-28'],
                'nodes': [
                    {
                        'text': 'LiteralGenre',
                        'tags': ['2018-08-28'],
                    },
                    {
                        'text': 'FineArtGen',
                        'tags': ['2018-08-28'],
                    },
                ]
            }
        ]
    }

    re_add_href(schema_data)
    return json.dumps([schema_data])


def re_add_href(node):
    node['href'] = '/graph/schema/query?className=' + node['text']

    if 'nodes' not in node:
        return
    else:
        for child_node in node['nodes']:
            re_add_href(child_node)


def get_schema_class(class_name):
    class_data = [
        {
            'name': 'Thing',
            'value': 'Thing',
            'desc': '所有类的基类'
        },
        {
            'name': 'Thing',
            'value': 'Thing',
            'desc': '所有类的基类'
        }
    ]

    return class_data
