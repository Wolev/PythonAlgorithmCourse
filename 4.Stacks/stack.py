# Stack data structure implementation

class Stack:

    def __init__(self):
        self.stack = []  # use a 1D array as an underlying data structure

    # PUSH method
    def push(self, data):
        '''Insert item into the stack'''
        self.stack.append(data)

    # POP method
    # O(1) constant running time
    def pop(self):
        '''Remove and return the last item inserted [LIFO]'''
        data = self.stack[-1]
        del  self.stack[-1]
        return data

    # PEEK method
    # O(1) constant running time
    def peek(self):
        '''Returns the last item without removing it'''
        return self.stack[-1]

    def is_empty(self):
        '''Check if the stack is empty or not'''
        return self.stack == []

    def stack_size(self):
        return len(self.stack)


if __name__ == "__main__":

    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print("Size: %d" % stack.stack_size())
    print("Poped: %d" %stack.pop())
    print("Size: %d" % stack.stack_size())
    print("Peek: %d" % stack.peek())
    print("Size: %d" % stack.stack_size())
    print("Poped: %d" % stack.pop())