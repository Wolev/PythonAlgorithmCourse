class Node:
    def __init__(self, data):
        self.data = data  # stores data
        self.nextNode = None  # reference to the next Node

class LinkedList:
    def __init__(self):
        self.head = None  # the head has no value
        self.numOfNodes = 0  # reference to the number of nodes

    # How to insert a node at the beginning: O(1) running time
    def insert_start(self, data):

        self.numOfNodes += 1 # add a node
        new_node = Node(data)

        if not self.head:
            self.head = new_node  # linked list is empty and this is the first node
        else:  # the linked list is not empty case
            new_node.nextNode = self.head  # creates a new node
            self.head = new_node  # the head is the new node

    # How to insert a node at the end: O(N) running time
    def insert_end(self, data):

        self.numOfNodes += 1
        new_node = Node(data)

        # Point to the head of the LinkedList
        actual_node = self.head

        # Find the last node of the Linked List
        while actual_node.nextNode is not None:
            # Go from node to node until last node is reached
            actual_node = actual_node.next

        # Makes sure that the actual node is equal to the new node
        # After finding the last node, you insert the new Node
        actual_node.nextNode = new_node

    # How many nodes are there in the linked list
    #
    def size_of_linkedlist(self):
        return self.numOfNodes

    # Traverse the linked list
    # Linear time complexity O(N)
    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next

    def remove(self, data):

        # if the data structure is empty you return
        if self.head is None:
            return

        actual_node = self.head  # actual node initialised as the first node
        previous_node = None  # the previous node intialised to be None

        # Search for the item you want to remove
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next

        # Search miss - the item isn't in the list
        if actual_node is None:
            return

        # decrease the number of nodes
        self.numOfNodes -= 1

        # Search found, you get two options
        if previous_node is None:
            # the node found is the first node
            self.head = actual_node.next
        else:
            # the node found is an internal node
            # Remove the internal node from the linked list
            previous_node.nextNode = actual_node.next

linked_list = LinkedList()
linked_list.insert_start(4)
linked_list.insert_start(3)
linked_list.insert_start(1)
linked_list.insert_start(8)
linked_list.insert_end(10)
linked_list.insert_end(100)
linked_list.insert_end(1000)

print("The size of the linked list is %d" %linked_list.size_of_linkedlist())
linked_list.traverse()
linked_list.remove(3)


print("--------------")
linked_list.traverse()
print("The size of the linked list is %d" %linked_list.size_of_linkedlist())