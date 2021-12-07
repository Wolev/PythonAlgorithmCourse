# Linked List Interview Question #7
# Construct an algorithm that's able to find the middle node and traverse the list using two pointers

class Node:
    def __init__(self, data):
        self.data = data
        self.head = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


    def insert(self, data):
        self.numOfNodes