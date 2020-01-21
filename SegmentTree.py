# https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/tutorial/
# Algorithm taken from above link
# Complete
# Sum of range of elements in range

from collections import defaultdict


class SegmentTree:
    def __init__(self, input_list):
        self.list_ = input_list.copy()
        self.list_length = len(input_list)
        # self.segment_tree = [0] * (2 * self.list_length)
        self.segment_tree = defaultdict(int)
        self.BuildTree(1, 0, self.list_length - 1)

    def BuildTree(self, node, start_index, end_index):
        if start_index == end_index:
            self.segment_tree[node] = self.list_[start_index]
            return

        mid = (start_index + end_index) // 2
        self.BuildTree(2 * node, start_index, mid)
        self.BuildTree(2 * node + 1, mid + 1, end_index)

        self.segment_tree[node] = self.segment_tree[2 * node] + self.segment_tree[2 * node + 1]

    def UpdateTree(self, index, value):

        old_value = self.list_[index]
        self.list_[index] = value

        node = 1
        diff = value - old_value
        self.segment_tree[node] += diff

        left = 0
        right = self.list_length - 1

        while left < right:
            mid = (left + right) // 2
            if index > mid:
                left = mid + 1
                node = 2 * node + 1

            else:
                right = mid
                node = 2 * node

            self.segment_tree[node] += diff

    def SearchSegmentTree(self, node, node_left, node_right, query_left, query_right):
        mid = (node_left + node_right) // 2
        if query_left <= node_left <= node_right <= query_right:
            return self.segment_tree[node]

        elif (query_left <= query_right < node_left) or (node_right < query_left <= query_right):
            return 0

        else:
            mid = (node_left + node_right) // 2
            return self.SearchSegmentTree(2 * node, node_left, mid, query_left, query_right) \
                   + self.SearchSegmentTree(2 * node + 1, mid + 1, node_right, query_left, query_right)

    def QueryTree(self, query_left, query_right):
        if not 0 <= query_left <= query_right <= self.list_length:
            return -1

        return self.SearchSegmentTree(1, 0, self.list_length - 1, query_left, query_right)

    def PrintTree(self):
        i = 1
        while i <= 2 * self.list_length - 1:
            print(self.segment_tree[i], end=" ")
            i += 1


def main():
    list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    seg_tree = SegmentTree(list_)
    seg_tree.PrintTree()
    seg_tree.UpdateTree(1, 20)
    seg_tree.UpdateTree(2, 20)
    seg_tree.UpdateTree(0, 20)
    seg_tree.UpdateTree(3, 20)
    seg_tree.UpdateTree(4, 20)
    seg_tree.UpdateTree(5, 20)
    seg_tree.UpdateTree(6, 20)
    seg_tree.UpdateTree(7, 20)
    seg_tree.UpdateTree(8, 20)
    seg_tree.UpdateTree(9, 20)
    print()
    seg_tree.PrintTree()
    print()
    print(seg_tree.QueryTree(0, 9))
    print(seg_tree.QueryTree(1, 9))
    print(seg_tree.QueryTree(2, 5))
    print(seg_tree.QueryTree(4, 7))
    print(seg_tree.QueryTree(6, 6))


if __name__ == '__main__':
    main()
