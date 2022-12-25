# this is code for reversing a linked list


class Node:
    def __init__(self, key):
        self.next = None
        self.key = key


head_node = None
temp_head = None


def InsertNode(input_key):
    global head_node
    if head_node is None:
        head_node = Node(input_key)

    else:
        temp = head_node
        while temp.next:
            temp = temp.next

        temp.next = Node(input_key)


def DisplayLL(input_node):
    temp = input_node
    while temp:
        print(temp.key, end=" ")
        temp = temp.next


def ReverseLL(input_node):
    global head_node0
    if input_node.next is None:
        head_node = input_node
        return input_node

    ReverseLL(input_node.next).next = input_node
    if input_node == temp_head:
        input_node.next = None


def main():
    InsertNode(10)
    InsertNode(40)
    InsertNode(30)
    InsertNode(70)
    InsertNode(60)
    DisplayLL(head_node)
    print()
    ReverseLL(head_node)
    temp_head = head_node
    DisplayLL(head_node)


if __name__ == '__main__':
    main()