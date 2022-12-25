# Code to clone a linked list


class Node:
    def __init__(self, key):
        self.next = None
        self.key = key


head_node = None


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


def DuplicateLL():
    if head_node is None:
        return
    # Inserting copy of previous node in ll for ex: 10 -> 20 -> None becomes 10 -> 10 -> 20 -> 20 -> None
    temp = head_node
    temp_next = temp.next

    while temp_next:
        temp.next = Node(temp.key)
        temp = temp.next
        temp.next = temp_next

        temp = temp.next
        temp_next = temp_next.next

    temp.next = Node(temp.key)
    temp.next.next = None

    # separating the two linked lists
    new_head = head_node.next
    temp = head_node
    temp_next = new_head

    while temp_next.next:
        temp.next = temp_next.next
        temp = temp.next

        temp_next.next = temp.next
        temp_next = temp_next.next

    temp.next = None
    temp_next.next = None

    return new_head


def main():

    InsertNode(10)
    InsertNode(40)
    InsertNode(30)
    InsertNode(70)
    InsertNode(60)
    DisplayLL(head_node)
    print()
    cloned_ll = DuplicateLL()
    DisplayLL(cloned_ll)
    print()


if __name__ == '__main__':
    main()