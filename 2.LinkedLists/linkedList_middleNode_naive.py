# Linked List Interview Question #7
# Construct an algorithm that's able to find the middle node and traverse the list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_start(self, data):
        self.size += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def size_of_linkedList(self):
        return self.size

    def traverse(self):
        actual_node = self.head

        print("----------")
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next
        print("----------")



    def middle_node(self):
        actual_node = self.head
        sizeofNode = 0

        while actual_node is not None:
            if sizeofNode == self.size // 2:
                print("This is the middle node: " + str(actual_node))
                print("This is the middle node data: " + str(actual_node.data))
                break
            else:
                actual_node = actual_node.next
                sizeofNode += 1

if __name__ == "__main__":

    linked_list = LinkedList()

    linked_list.insert_start(0)
    linked_list.insert_start(1)
    linked_list.insert_start(2)
    linked_list.insert_start(3)
    linked_list.insert_start(4)
    linked_list.insert_start(5)
    linked_list.insert_start(6)

    print("The size of the list is:  %d" % linked_list.size_of_linkedList())
    linked_list.middle_node()
    linked_list.traverse()