# -*- coding: utf-8 -*-
import json
from flask import render_template, request, jsonify

from application.models.graph.dbalchemy import DbAlchemy
from application.controller.graph.service.schema_service import SchemaService
from . import graph_blueprint

from .service.entity_service import request_a_entity, request_all_entity_labels, save_entity_label
from .service.lemma_service import random_entity
from .service.relation_service import request_a_relation, request_all_relation_type, save_relation_label, creat_relation_instances


"""
Services that will be initialized only once
"""
schema_service = SchemaService()
neo4j_alchemy = DbAlchemy()


"""
Request pages
"""
@graph_blueprint.route('/')
def graph():
    return render_template('main/graph.html')


@graph_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        data_source = neo4j_alchemy.initialize_graph()
        return render_template('graph/search.html', data_source=data_source)
    elif request.method == 'POST':
        name = request.form['mention']
        data_source = neo4j_alchemy.retrieve_by_name(name)
        return render_template('graph/search.html', data_source=data_source)


@graph_blueprint.route('/contributor')
def contributor():
    return render_template('graph/contributor.html')


@graph_blueprint.route('/schema')
def schema():
    schema_data = schema_service.query_schema()
    return render_template('graph/schema/schema.html', schema_data=schema_data)


@graph_blueprint.route('/schema/query')
def schema_query():
    if request.method == 'GET':
        class_name = request.args.get('className')
        class_properties = schema_service.query_a_entity_schema(class_name)
        return render_template('graph/schema/schema_class.html', class_name=class_name, class_properties=class_properties)


@graph_blueprint.route('/document')
def graph_document():
    return render_template('graph/document/label.html')


@graph_blueprint.route('/entity')
def tag_entity():
    _, entity_sample = request_a_entity()
    label_data = request_all_entity_labels()
    data = {
        'entity_data': entity_sample,
        'label_data': label_data,
    }
    return render_template('graph/tagger/entity.html', data=data)


@graph_blueprint.route('/next_entity', methods=['GET'])
def tag_entity_next():
    text_id = request.args.get('id')
    _, entity_sample = request_a_entity(fromid=text_id)
    label_data = request_all_entity_labels()
    data = {
        'entity_data': entity_sample,
        'label_data': label_data,
    }
    return jsonify(data)


@graph_blueprint.route('/entity_label', methods=['POST'])
def tag_entity_label():
    if request.method == 'POST':
        text_id = request.form['text_id']
        labels = json.loads(request.form['labels'])
        mark = request.form['mark']
        relation_instances = save_entity_label(text_id, labels, mark)

        creat_relation_instances(relation_instances)

        return "标注成功"


@graph_blueprint.route('/relation')
def tag_relation():
    relation_sample = request_a_relation(0)
    all_relations = request_all_relation_type()
    data = {
        "relation_data": relation_sample,
        "relation_types": all_relations,
    }
    return render_template('graph/tagger/relation.html', data=data)


@graph_blueprint.route('/next_relation', methods=['GET'])
def tag_relation_next():
    sentence_id = request.args.get('id')
    relation_sample = request_a_relation(fromid=sentence_id)
    all_relations = request_all_relation_type()
    data = {
        "relation_data": relation_sample,
        "relation_types": all_relations,
    }
    return jsonify(data)


@graph_blueprint.route('/relation_label', methods=['GET', 'POST'])
def tag_relation_label():
    if request.method == 'GET':
        sentence_id = request.args.get('sentence_id')
        relation_id = request.args.get('relation_id')
        mark = request.args.get('mark')
        save_relation_label(sentence_id, relation_id, mark)

        return '标注成功'

@graph_blueprint.route('/lemma')
def tag_lemma():
    lemma_data = random_entity()
    return render_template('graph/tagger/lemma.html', entity_data=lemma_data)