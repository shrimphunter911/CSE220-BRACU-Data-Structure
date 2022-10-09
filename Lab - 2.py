class Node:
    def __init__(self, element, reference):
        self.elem = element
        self.next = reference


class MyList:
    def __init__(self, a = None):
        self.head = None
        tail = None

        if a is not None:
            for i in a:
                node = Node(i, None)
                if self.head is None:
                    self.head = node
                    tail = node
                else:
                    tail.next = node
                    tail = node

    def showlist(self):
        node = self.head
        while node is not None:
            print(node.elem, node.next)
            node = node.next

        if self.head is None:
            print('Empty list')

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def clear(self):
        node = self.head
        self.head = None
        while node is not None:
            temp = node
            node = node.next
            temp.elem = None
            temp.next = None

    def insert(self, newElement):
        node = self.head
        turn = False
        temp = None
        while node is not None:
            temp = node
            if node.elem == newElement:
                turn = True
            node = node.next

        if not turn:
            temp.next = Node(newElement, None)

    def nodeAt(self, index):
        node = self.head
        i = 0
        while i < index:
            i += 1
            node = node.next
        return node

    def insertAt(self, newElement, index):
        node = self.head
        turn = False
        temp = None
        while node is not None:
            temp = node
            if node.elem == newElement:
                turn = True
            node = node.next

        if not turn:
            if index == 0:
                newNode = Node(newElement, self.head)
                self.head = newNode
            else:
                prevNode = self.nodeAt(index-1)
                newNode = Node(newElement, prevNode.next)
                prevNode.next = newNode

    def remove(self, deletekey):
        if deletekey == 0:
            old = self.head
            value = old.elem
            self.head = old.next
        else:
            prevNode = self.nodeAt(deletekey-1)
            old = prevNode.next
            value = old.elem
            prevNode.next = old.next

        old.elem = None
        old.next = None
        return value

    def even(self):
        node = self.head
        evenLinked = MyList()
        tail = None
        while node is not None:
            if node.elem % 2 == 0:
                n = Node(node.elem, None)
                if evenLinked.head is None:
                    evenLinked.head = n
                    tail = n
                else:
                    tail.next = n
                    tail = n
            node = node.next
        return evenLinked

    def find(self, element):
        node = self.head
        turn = False
        while node is not None:
            if node.elem == element:
                turn = True
                break
            else:
                turn = False
            node = node.next
        return turn

    def reverse(self):
        node = self.head
        newHead = None
        while node is not None:
            next = node.next
            node.next = newHead
            newHead = node
            node = next
        self.head = newHead

    def sum(self):
        node = self.head
        sum = 0
        while node is not None:
            sum = sum + node.elem
            node = node.next
        return sum


# Tester Class
list1 = [1, 2, 3, 4, 5]
list2 = MyList(list1)
list2.showlist()
print(list2.isEmpty())
list2.clear()
list2.showlist()
print(list2.isEmpty())
list1 = [1, 2, 3, 4, 5]
list2 = MyList(list1)
list2.showlist()
list2.insert(1)
list2.insert(3)
list2.insert(6)
list2.showlist()
list2.insertAt(0, 0)
list2.showlist()
list2.insertAt(0, 2)
list2.showlist()
list2.insertAt(16, 2)
list2.showlist()
list2.remove(2)
list2.showlist()
even = list2.even()
even.showlist()
print(list2.find(4))
even.reverse()
even.showlist()
print(even.sum())