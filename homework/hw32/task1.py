# Modify the 'depth-first search' to produce strongly connected components (Strongly Connected Components ).


from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.DFS(i, visited, stack)
        stack.append(v)

    def get_transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def SCC(self):
        visited = [False] * (self.V)
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.DFS(i, visited, stack)

        reversed_graph = self.get_transpose()

        visited = [False] * (self.V)
        scc_list = []

        while stack:
            v = stack.pop()
            if not visited[v]:
                scc = []
                reversed_graph.DFS(v, visited, scc)
                scc_list.append(scc)

        return scc_list


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(1, 3)
    g.add_edge(3, 4)

    print("Strongly Connected Components:")
    scc_list = g.SCC()
    for scc in scc_list:
        print(scc)
