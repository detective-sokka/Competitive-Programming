# My implementation of binary search tree


# Node class for Binary Search Tree

'''
8
10
20
50
70
90
220
120
150
'''


class Node:
    def __init__(self, key):
        self.key = key
        self.left_node = None
        self.right_node = None


class BSTree:
    def __init__(self):
        self.root = None

    def insertNode(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        prev = None
        temp = self.root

        while True:
            prev = temp
            if key > temp.key:
                temp = temp.right_node
            else:
                temp = temp.left_node

            if temp is None:
                if key > prev.key:
                    prev.right_node = Node(key)
                else:
                    prev.left_node = Node(key)

                return

    def InOrderTraversal(self, input_node):
        if input_node is None:
            return

        self.InOrderTraversal(input_node.left_node)
        print(input_node.key, end=" ")
        self.InOrderTraversal(input_node.right_node)

    def PreOrderTraversal(self, input_node):
        if input_node is None:
            return

        print(input_node.key, end=" ")
        self.PreOrderTraversal(input_node.left_node)
        self.PreOrderTraversal(input_node.right_node)

    def PostOrderTraversal(self, input_node):
        if input_node is None:
            return

        self.PostOrderTraversal(input_node.left_node)
        self.PostOrderTraversal(input_node.right_node)
        print(input_node.key, end=" ")

    def PrintTree(self):
        print("\nIn order traversal of tree is : ")
        self.InOrderTraversal(self.root)

        print("\nPre-order traversal : ")
        self.PreOrderTraversal(self.root)

        print("\nPost order traversal : ")
        self.PostOrderTraversal(self.root)

    def SearchNode(self, key):
        if self.root is None:
            return

        temp = self.root
        while temp:
            if key > temp.key:
                temp = temp.right_node
            elif key == temp.key:
                return True
            else:
                temp = temp.left_node

        return False


def main():
    bst = BSTree()
    print("\nNo of values to be input : ")
    N = int(input())
    while N > 0:
        bst.insertNode(int(input()))
        N -= 1

    bst.PrintTree()
    print()
    print(bst.SearchNode(120))
    print(bst.SearchNode(10))
    print(bst.SearchNode(1000))


if __name__ == "__main__":
    main()


