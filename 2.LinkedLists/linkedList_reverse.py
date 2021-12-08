# Interview Question #8
# Construct an in-place algorithm to reverse a linked list!
# Pointer method that achieves in-place algorithm with O(N) running time complexity
# 3 pointers: previous_node, next_node, current_node


class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # O(N) running time complexity
    def reverse_list(self):
        ''' Reverse the linked list using three pointers.'''

        current_node = self.head
        previous_node = None
        next_node = None

        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = previous_node  # The moment the reference is flipped
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def insert_start(self, data):
        self.size += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse_list(self):
        actual_node = self.head
        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node

if __name__ == "__main__":

    linked_list = LinkedList()

    linked_list.insert_start(12)
    linked_list.insert_start(122)
    linked_list.insert_start(3)
    linked_list.insert_start(31)
    linked_list.insert_start(10)
    linked_list.insert_start(11)

    print("\nNormal list: ")
    linked_list.traverse_list()
    linked_list.reverse_list()

    print("\nReversed list: ")
    linked_list.traverse_list()

