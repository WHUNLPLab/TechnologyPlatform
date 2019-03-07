# -*- coding:utf-8 -*-
from py2neo import Graph

class KgGraph(object):
    """
    This class works on querying Neo4j database
    """

    def __init__(self):
        self.graph = None


    def connect_neo4j(self, database_uri):
        """
        Connect to Neo4j database
        :param database_uri: database_uri 
        :return:
        """
        self.graph = Graph(database_uri)


    def execute_cypher(self, ql):
        """
        Execute a cypher query
        :param ql: (string) cypher query
        :return: (list) a list of records
        """
        record_list = self.graph.data(ql)
        return record_list
