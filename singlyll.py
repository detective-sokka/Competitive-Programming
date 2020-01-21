# https://dev.to/erikkristoferanderson/singly-linked-list-a-python-implementation-4cm6

'''
Class to define a node in a singly linked list. It stores the following data.
    Data - Stores the data of the node
    Next - Pointer to the next node
'''


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_node):
        self.next_node = new_node

'''
Class to create a linked list. PS: new nodes are appended in the beginning of the linked list 
    head - stores the head of the linked list
'''


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        count_ = 0
        curr = self.head
        while curr:
            count_ += 1
            curr = curr.get_next()

        return count_

    def Print(self):
        curr = self.head
        while curr:
            print(curr.get_data(), end=" ")
            curr = curr.get_next()
        print()

    def Search(self, data):
        curr = self.head
        found = False

        while curr:
            if curr.data == data:
                found = True
                break
            curr = curr.get_next()

        return found

    def Delete(self, data):
        curr = self.head
        prev = None
        found = False

        while curr:
            if curr.get_data() == data:
                found = True
                break
            else:
                prev = curr
                curr = curr.get_next()

        if found:
            if prev is None:
                self.head = curr.get_next()
            else:
                prev.set_next(curr.get_next())

        return found


def main():
    third_node = Node(3)
    second_node = Node(2, third_node)
    first_node = Node(1, second_node)
    ll = LinkedList(first_node)
    ll.Print()

    ll.insert(5)
    ll.Print()
    print("Size of ll is : {}".format(ll.size()))

    if ll.Search(2):
        print("2 is found")
    if ll.Search(6):
        print("6 is not found")

    ll.Delete(1)
    ll.Print()

    ll.Delete(4)
    ll.Print()

    ll.Delete(5)
    ll.Print()


if __name__ == '__main__':
    main()