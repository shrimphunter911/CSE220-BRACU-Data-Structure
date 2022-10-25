class Stack_Array:
    stack = []
    pointer = -1

    def push(self, element):
        self.stack.append(element)
        self.pointer += 1

    def peek(self):
        return self.stack[self.pointer]

    def pop(self):
        value = self.stack[self.pointer]
        self.stack = self.stack[:-1]
        self.pointer -= 1
        return value


stack1 = Stack_Array()
stack1.push(2)
print(stack1.peek())
stack1.push(5)
print(stack1.peek())
stack1.pop()
print(stack1.peek())


class Node:
    def __init__(self, elem):
        self.elem = elem
        self.prev = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, elem):
        if self.head is None:
            self.head = Node(elem)
        else:
            n = Node(elem)
            n.prev = self.head
            self.head = n

    def peek(self):
        return self.head.elem

    def pop(self):
        old = self.head
        self.head = old.prev

        old.prev = None
        return old.elem

stack = Stack()
stack.push(1)
print(stack.peek())
stack.push(2)
print(stack.peek())
stack.pop()
print(stack.peek())
