# -*- coding:utf-8 -*-
from .kggraph import KgGraph
from flask import current_app
from manage import app


class DbAlchemy(object):

    def __init__(self):
        self.graph = KgGraph()

        with app.app_context():
            self.graph.connect_neo4j(current_app.config['NEO4J_DATABASE_URI'])

    def initialize_graph(self):
        """
        Select all nodes and relations in graph
        :return: json result
        """
        #nodes = self.graph.execute_cypher('MATCH (n) RETURN n LIMIT 30')
        #edges = self.graph.execute_cypher('MATCH ()-[r]->() RETURN r')

        records = self.graph.execute_cypher('MATCH (n)-[r]->(m) RETURN n, r, m LIMIT 150')
        nodes = []
        edges = []
        for record in records:
            nodes.append(record['n'])
            nodes.append(record['m'])
            edges.append(record['r'])

        nodes = map(self._buildNodes, nodes)
        edges = map(self._buildEdges, edges)

        return self._export_alchemyjs(nodes, edges)

    def retrieve_by_name(self, name):
        """
        Retrieve a node and its relations by name
        :param name: name property
        :return:
        """

        nodes = []
        edges = []

        cql = 'MATCH (n {{name: "{0}"}})-[r]->(m) RETURN n, r, m'.format(name)
        records = self.graph.execute_cypher(cql)

        for record in records:
            nodes.append(record['n'])
            nodes.append(record['m'])
            edges.append(record['r'])

        cql = 'MATCH (n)-[r]->(m {{name: "{0}"}}) RETURN n, r, m'.format(name)
        records = self.graph.execute_cypher(cql)

        for record in records:
            nodes.append(record['n'])
            nodes.append(record['m'])
            edges.append(record['r'])

        nodes = map(self._buildNodes, nodes)
        edges = map(self._buildEdges, edges)

        return self._export_alchemyjs(nodes, edges)


    def _export_alchemyjs(self, nodes, edges):
        """
        Export record results for Alchemy.js
        :param nodes: graph nodes
        :param edges: graph edges
        :return: json data
        """
        nodes = [node for node in nodes]
        edges = [edge for edge in edges]

        json = {"nodes": nodes, "edges": edges}

        return json


    def _buildNodes(self, nodeRecord):
        data = {"id": nodeRecord['identifier'], "label": nodeRecord['labels']}
        data.update(nodeRecord.properties)

        return data


    def _buildEdges(self, relationRecord):
        data = {"source": relationRecord['source'],
                "target": relationRecord['target'],
                "relationship": relationRecord['label']}

        return data