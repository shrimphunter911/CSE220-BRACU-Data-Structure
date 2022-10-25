class Stack_Array:
    def __init__(self):
        self.stack = []
        self.pointer = -1

    def push(self, elem):
        self.stack.append(elem)
        self.pointer += 1

    def peek(self):
        return self.stack[self.pointer]

    def pop(self):
        element = self.stack[self.pointer]
        self.stack = self.stack[:-1]
        self.pointer -= 1
        return element


# Task 1

def balance1(string):
    count = 0
    counter = []
    stack = Stack_Array()
    for char in string:
        count += 1
        if char == '(' or char == '{' or char == '[':
            stack.push(char)
            counter.append(count)
        elif char == ')' or char == '}' or char == ']':
            if not counter:
                print('This expression is NOT correct.')
                print('Error at character #', str(count) + '.', char, '- not opened.')
                return
            else:
                if char == ')':
                    if stack.peek() == '(':
                        stack.pop()
                        counter.pop()
                    else:
                        print('This expression is NOT correct.')
                        print('Error at character #', str(counter.pop()) + '.', stack.peek(), '- not closed.')
                        return
                elif char == '}':
                    if stack.peek() == '{':
                        stack.pop()
                        counter.pop()
                    else:
                        print('This expression is NOT correct.')
                        print('Error at character #', str(counter.pop()) + '.', stack.peek(), '- not closed.')
                        return
                elif char == ']':
                    if stack.peek() == '[':
                        stack.pop()
                        counter.pop()
                    else:
                        print('This expression is NOT correct.')
                        print('Error at character #', str(counter.pop()) + '.', stack.peek(), '- not closed.')
                        return
    if not counter:
        print('This expression is correct.')
        return


text1 = '1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'
balance1(text1)


# Task 2

class Node:
    def __init__(self, elem):
        self.elem = elem
        self.prev = None


class Stack_Linked:
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


def balance2(string):
    count = 0
    counter = []
    stack = Stack_Linked()
    for char in string:
        count += 1
        if char == '(' or char == '{' or char == '[':
            stack.push(char)
            counter.append(count)
        elif char == ')' or char == '}' or char == ']':
            if not counter:
                print('This expression is NOT correct.')
                print('Error at character #', str(count) + '.', char, '- not opened.')
                return
            else:
                if char == ')':
                    if stack.peek() == '(':
                        stack.pop()
                        counter.pop()
                    else:
                        print('This expression is NOT correct.')
                        print('Error at character #', str(counter.pop()) + '.', stack.peek(), '- not closed.')
                        return
                elif char == '}':
                    if stack.peek() == '{':
                        stack.pop()
                        counter.pop()
                    else:
                        print('This expression is NOT correct.')
                        print('Error at character #', str(counter.pop()) + '.', stack.peek(), '- not closed.')
                        return
                elif char == ']':
                    if stack.peek() == '[':
                        stack.pop()
                        counter.pop()
                    else:
                        print('This expression is NOT correct.')
                        print('Error at character #', str(counter.pop()) + '.', stack.peek(), '- not closed.')
                        return

    if not counter:
        print('This expression is correct.')
        return


text2 = '1+2*(3/4)'
balance2(text2)
