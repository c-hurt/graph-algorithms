# add exceptions
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,s,d):
        self.graph[s].append(d)

    # recursive dfs implementation
    def _dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex)

        for v in self.graph[vertex]:
            if visited[v] == False:
                self._dfs_util(v, visited)

    def dfs(self, vertex):
        visited = [False] * len(self.graph)

        self._dfs_util(vertex, visited)

graph_parse = Graph()
graph_use = [1, 2, 3, 5, 0, 4]
graph_link = [2, 3, 4, 5, 1, 0]

for s in graph_use:
    for d in graph_link:
        graph_parse.addEdge(s, d)

print('--- DFS ---')
graph_parse.dfs(0)