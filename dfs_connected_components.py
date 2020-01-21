# https://www.youtube.com/watch?v=09_LlHjoEiY&t=1310s
# DFS algorithm to find number of connected components

'''
Test case :
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(0, 3)
graph.addEdge(1, 2)
graph.addEdge(2, 3)
graph.addEdge(4, 5)
graph.addEdge(4, 6)
graph.addEdge(5, 6)
graph.addEdge(6, 1)

'''


from collections import defaultdict
import numpy as np


class Graph:
    def __init__(self, n):
        self.num_nodes = n
        self.adj_list = defaultdict(list)
        self.visited = []
        self.components_count = 0
        self.components = []

    def addEdge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def DFS(self, start_node):
        self.visited[start_node] = True
        self.components[start_node] = self.components_count

        for node_ in self.adj_list[start_node]:
            if not self.visited[node_]:
                self.DFS(node_)

    def findComponents(self):
        # Resetting the visited list
        self.visited = np.zeros(self.num_nodes, dtype=bool)
        self.components = np.zeros(self.num_nodes, dtype=int)

        self.components_count = 0

        for i in range(self.num_nodes):
            if not self.visited[i]:
                self.components_count += 1
                self.DFS(i)

    def printComponents(self):
        self.findComponents()
        print(self.components_count)
        print(self.components)


def main():

    graph = Graph(7)
    graph.addEdge(0, 1)
    # graph.addEdge(0, 2)
    # graph.addEdge(0, 3)
    graph.addEdge(1, 2)
    # graph.addEdge(2, 3)
    graph.addEdge(3, 3)
    graph.addEdge(4, 5)
    graph.addEdge(4, 6)
    graph.addEdge(5, 6)
    # graph.addEdge(6, 1)

    graph.printComponents()


if __name__ == "__main__":
    main()

