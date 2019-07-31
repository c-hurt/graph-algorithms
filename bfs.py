from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, source, dest):
        self.graph[source].append(dest)

    def bfs(self, source):
        visited = [False] * len(self.graph)
        queue = []

        queue.append(source)
        visited[source] = True

        print('-- BFS --')

        while queue:
            next =  queue.pop()
            print(next)

            for vertex in self.graph[next]:
                if not visited[vertex]:
                    queue.append(vertex)
                    visited[vertex] = True

graph_parse = Graph()
graph_use = [1, 2, 3, 5, 0, 4]
graph_link = [2, 3, 4, 5, 1, 0]

for v in graph_use:
    for d in graph_link:
        graph_parse.addEdge(v,d)

graph_parse.bfs(2)