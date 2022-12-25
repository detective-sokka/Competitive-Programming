# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

from collections import defaultdict
import numpy as np


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)
        self.visited = []

    def addEdge(self, u, v):
        self.adj_list[u].append(v)

    def computeGraph(self):
        self.visited = np.zeros(len(self.adj_list), dtype=bool)

    def computeDFS(self, start_node):
        print(start_node, end=" ")
        self.visited[start_node] = True
        for element in self.adj_list[start_node]:
            if not self.visited[element]:
                self.computeDFS(element)

    def DFS(self, start_node):
        if start_node < len(self.adj_list):
            self.computeGraph()
            print("The following is the order in which DFS encounters nodes: ", end=" ")
            self.computeDFS(start_node)
            print()
        else:
            print("The node entered doesn't exist")


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(4, 4)
g.DFS(0)
g.DFS(1)
g.DFS(2)
g.DFS(3)
g.DFS(4)
g.DFS(5)