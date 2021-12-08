# Interview Question #8
# Construct an in-place algorithm to reverse a linked list!

class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        self.size += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node
