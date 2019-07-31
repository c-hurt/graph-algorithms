from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)

    def addEdge(self, s, d):
        self.graph[s].append(d)

    def get_parent(self, parent, a):
        if parent[a] == -1:
            return a
        return self.get_parent(parent, parent[a])

    def union(self, parent, a, b):
        a_set = self.get_parent(parent,a)
        b_set = self.get_parent(parent,b)

        parent[a_set] = b_set


    def check_cycle(self):
        parent = [-1] * self.num_vertices

        for c in self.graph:
            for d in self.graph[c]:
                a_parent = self.get_parent(parent,c)
                b_parent = self.get_parent(parent,d)

                if a_parent == b_parent:
                    return True
                self.union(parent, c, d)
        return False


graph_check = Graph(4)
edges = [(0,1), (2,0), (3,0), (2,3)]

for (a,b) in edges:
    graph_check.addEdge(a, b)

print(graph_check.graph)
print(graph_check.check_cycle())