# Linked List Interview Question #7
# Construct an algorithm that's able to find the middle node and traverse the list using two pointers

class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0

    # The function to get the middle node
    # Get a fast pointer that moves 2x as fast as slow pointer
    # When the fast pointer reaches the end of the list, the small pointer is the middle node

    # Linear running time complexity: O(n) = N
    def get_middle_node(self):

        fast_pointer = self.head
        slow_pointer = self.head

        # Similarly we can write just fast_pointer.nextNode without the is not None because it's implied
        #while fast_pointer.next_node is not None and fast_pointer.next_node.next_node is not None:
        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            # this slow_pointer will point to the middle node when the loop stops

            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

            return slow_pointer

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
            actual_node = actual_node.next

if __name__ == "__main__":

    linked_list = LinkedList()

    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)

    print(linked_list.get_middle_node().data)
