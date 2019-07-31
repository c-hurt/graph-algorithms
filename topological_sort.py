from collections import defaultdict


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)

    def edgeAdd(self,s,d):
        self.graph[s].append(d)

    def edgeAddAll(self, edges):
        for (a,b) in edges:
            self.edgeAdd(a,b)

    def _topological_sort_util(self,vertex,visited,stack):
        visited[vertex] = True

        for a in self.graph[vertex]:
            if not visited[a]:
                self._topological_sort_util(a,visited,stack)
        stack.insert(0,vertex)

    def topological_sort(self):
        visited = [False] * self.num_vertices
        stack = []

        for a in range(0, self.num_vertices):
            if not visited[a]:
                self._topological_sort_util(a,visited, stack)

        print(stack)


edges = [(0,1), (1,2), (2,3), (3,4), (5,4)]
graph_topological = Graph(6)
graph_topological.edgeAddAll(edges)

print(graph_topological.graph)
graph_topological.topological_sort()