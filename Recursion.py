def len_of_strings(s):
    if s == '':
        return 0
    else:
        return 1+len_of_strings(s[1:])


s = "Hia"
print(len_of_strings(s))


class Node:
    def __init__(self, elem, next):
        self.elem = elem
        self.next = next

    def show(self):
        print(self.elem, self.next)

    def length(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.length(node.next)


def length(node):
    if node is None:
        return 0
    else:
        return 1 + length(node.next)


d = Node(4, None)
c = Node(3, d)
b = Node(2, c)
a = Node(1, b)

n = a
while n is not None:
    n.show()
    n = n.next

node = a
print(length(node))


def sum_of_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_natural(n-1)


print(sum_of_natural(10))


def exponent(a, n):
    if n == 0:
        return 1
    else:
        return a * exponent(a, n-1)


print(exponent(2, 3))


def sum_of_digits(num, sum):
    if num == 0:
        return sum
    return sum_of_digits(int(num / 10), sum+(num % 10))


print(sum_of_digits(1234, 0))


def fact(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num*fact(num-1)


print(fact(4))