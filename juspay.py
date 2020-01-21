from collections import defaultdict

'''
class MTree
    Stores the m-ary tree.
    node_list - list of nodes in a tree
    m - 'm' value
'''


class MTree:
    def __init__(self, input_tree, m):
        # input_tree contains a list of nodes
        self.nodes = defaultdict(list)
        # dictionary holds a list of the following format [lock_order, lock_count]
        for node_index in input_tree:
            self.nodes[node_index] = [0, 0]
        self.m_val = m

    def LockNode(self, node_pos):
        lock_status = False
        i = node_pos

        if self.nodes[node_pos][0] != 0:
            return lock_status

        parent = (i-1) // self.m_val
        while parent >= 0:
            if self.nodes[parent][0] == 2:
                break
            elif self.nodes[parent][0] == 1:
                return lock_status
            parent = (parent - 1) // self.m_val

        lock_status = True

        if lock_status:
            i = node_pos
            self.nodes[i][0] = 1
            parent = (i - 1) // self.m_val
            while parent >= 0:
                self.nodes[parent][0] = 2
                self.nodes[parent][1] += 1
                parent = (parent - 1) // self.m_val

        return lock_status

    def UnlockNode(self, node_pos):
        unlock_status = False
        if self.nodes[node_pos][0] != 1:
            return unlock_status

        self.nodes[node_pos][0] = 0

        i = node_pos
        parent = (i - 1) // self.m_val

        while parent >= 0:
            if self.nodes[parent][0] == 2:
                self.nodes[parent][1] -= 1
                if self.nodes[parent][1] == 0:
                    self.nodes[parent][0] = 0

            parent = (parent - 1) // self.m_val

        return unlock_status


def main():
    # defining an 4-ary tree stored in an array format and the
    # node indexes of filled nodes are mentioned in position list.
    # For every node with index T (say), the index of children nodes are T * m + 1 to (T + 1) * m

    position_list = [0, 1, 2, 3, 7, 10, 29, 42]
    # storing all the nodes as a list, along with the m value in object of MTree class

    mtree = MTree(position_list, 4)
    mtree.LockNode(42)
    mtree.LockNode(1)
    mtree.LockNode(3)
    mtree.LockNode(7)
    mtree.LockNode(29)
    mtree.UnlockNode(10)
    mtree.UnlockNode(42)


if __name__ == "__main__":
    main()
