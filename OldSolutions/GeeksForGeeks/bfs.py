from collections import defaultdict
import numpy as np


class Graph:
    def __init__(self, num_nodes):
        self.nodes = defaultdict(list)
        self.num_nodes = num_nodes
        self.queue = []
        self.visited = []

    def SetupGraph(self):
        self.visited = np.zeros(self.num_nodes, dtype=bool)

    def AddNode(self, startnode, endnode):
        self.nodes[startnode].append(endnode)

    def ComputeBFS(self, startnode):
        self.queue.append(startnode)
        self.visited[startnode] = True

        while self.queue:
            node = self.queue.pop(0)
            print(node)

            for element in self.nodes[node]:
                if not self.visited[element]:
                    self.queue.append(element)
                    self.visited[element] = True

    def BFS(self, start_node):
        print(self.nodes)
        if start_node < self.num_nodes:
            self.SetupGraph()
            print("The following is the order in which BFS encounters nodes: ", end=" ")
            self.ComputeBFS(start_node)
            print()
        else:
            print("The node entered doesn't exist")


def main():
    g = Graph(4)
    g.AddNode(0, 1)
    g.AddNode(0, 2)
    g.AddNode(1, 2)
    g.AddNode(2, 0)
    g.AddNode(2, 3)
    g.BFS(0)
    g.BFS(1)
    g.BFS(2)
    g.BFS(3)
    g.BFS(4)


if __name__ == "__main__":
    main()