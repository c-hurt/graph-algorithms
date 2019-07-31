# implement version with priority queue
# add exceptions to check if empty

import sys
from collections import defaultdict
from collections import namedtuple

Edge = namedtuple('Edge', 'source dest weight')

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)

    def edgeAdd(self, edge):
        self.graph[edge.source].append((edge.dest, edge.weight))

    def getMinKey(self, key, visited):
        min_weight = sys.maxsize
        index = None

        for vertex in self.graph[key]:
            if vertex[0]


    def mst_find(self):
        mst_found = [None] * self.num_vertices
        visited = [False] * self.num_vertices

        # use first node to check for min edge
        visited[0] = True

        for vertex in range(self.num_vertices):
            if

graph_primm = Graph(3)
graph_primm.edgeAdd(Edge(source=0, dest=1, weight=10))
graph_primm.edgeAdd(Edge(source=1, dest=2, weight=20))

print(graph_primm.graph)