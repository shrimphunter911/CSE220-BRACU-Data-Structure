class Node:
    def __init__(self, elem, next, prev):
        self.elem = elem
        self.next = next
        self.prev = prev

class DoublyList:
    def __init__(self, a):
        self.head = None
        self.head = Node(None, None, None)
        head = self.head
        head.next = head.prev = head

        if a is not None:
            for i in a:
                node = Node(i, None, None)
                node.next = head.next
                node.prev = head
                head.next = node
                n = node.next
                n.prev = node
                head = node

    def showList(self):
        head = self.head
        node = head.next
        if node.elem is None:
            print('Empty List')
        else:
            while node is not head:
                print(node.elem, node.prev, node.next)
                node = node.next

    def showReverse(self):
        head = self.head
        node = head.prev
        while node is not head:
            print(node.elem, node.prev, node.next)
            node = node.prev

    def duplicateCheck(self, newElement):
        head = self.head
        node = head.next
        turn = False
        while node is not head:
            if node.elem == newElement:
                turn = True
            node = node.next
        return turn

    def insert(self, newElement):
        if not self.duplicateCheck(newElement):
            head = self.head
            node = Node(newElement, head, head.prev)
            n = head.prev
            n.next = node
            head.prev = node

    def nodeAt(self, index):
        i = 0
        head = self.head
        node = head.next
        while i < index:
            i += 1
            node = node.next
        return node

    def count(self):
        c = 0
        head = self.head
        node = head.next
        while node is not head:
            c += 1
            node = node.next
        return c

    def insertAt(self, newElement, index):
        if 0 <= index <= self.count():
            if not self.duplicateCheck(newElement):
                node = Node(newElement, None, None)
                prevNode = self.nodeAt(index-1)
                n = prevNode.next
                node.prev = prevNode
                node.next = n
                n.prev = node
                prevNode.next = node

    def remove(self, index):
        if 0 <= index <= self.count():
            prevNode = self.nodeAt(index-1)
            node = prevNode.next
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            node.elem = None
            node.next = None
            node.prev = None

    def removeKey(self, deletekey):
        head = self.head
        node = head.next
        while node is not head:
            if node.elem == deletekey:
                break
            node = node.next
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        node.next = None
        node.prev = None
        return node.elem


list1 = [1, 2, 3, 4, 5]
list2 = DoublyList(list1)
#list2.showReverse()
list2.insert(6)
n = list2.nodeAt(2)
print(n.elem)
print(list2.count())
list2.insertAt(6, 4)
list2.showList()
print('_________________')
list2.insertAt(7, 3)
list2.showList()
print('_________________')
print(list2.removeKey(7))
list2.showList()