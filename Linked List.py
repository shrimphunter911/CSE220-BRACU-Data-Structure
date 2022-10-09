class Node:
  def __init__(self, v, n):
    self.value = v
    self.next = n

  def printNode(self):
    print(self.value, '-', self.next)

class LinkedList:
  def __init__(self, head = None, tail = None):
    self.head = head
    self.tail = tail
  def convertlist(self, a):
    tail = self.tail
    for i in a:
      n = Node(i, None)
      if (self.head is None):
        self.head = n
        tail = n
      else:
        tail.next = n
        tail = n
    self.tail = tail
    
  def insertAtFirst(self, p):
    node = Node(p, self.head)
    self.head = node

  def insertAtEnd(self, p):
    node = Node(p, None)
    n = self.head
    while (n.next is not None):
      n = n.next
    n.next = node

  def printList(self):
    n = self.head
    while (n != None):
      n.printNode()
      n = n.next
  
  def count(self):
    c = 0
    n = self.head
    while (n != None):
      c += 1
      n = n.next
    return c

  def get(self, head, index):
    c = 0
    n = head
    while(n!=None):
      if c == index:
        n.printNode()
      c += 1
      n = n.next

  def set(self, elem, index):
    c = 0
    n = self.head
    while(n!=None):
      if c == index:
        n.value = elem
      c += 1
      n = n.next

  def nodeAt(self, index):
    node = self.head
    i = 0
    while(i < index):      
      node = node.next
      i += 1
    return node
  
  def searchValue(self, elem):
    n = self.head
    c = 0
    while(n is not None):
      if n.value == elem:
        return c
      c += 1
      n = n.next

  def insertAt(self, index, elem):
    if index == 0:
      node = Node(elem, self.head)
      self.head = node
    else:
      prev = self.nodeAt(index-1)
      node = Node(elem, prev.next)
      prev.next = node

  def remove(self, index):
    if index == 0:
      node = self.head
      self.head = node.next
    else:
      node = self.nodeAt(index)
      prev = self.nodeAt(index-1)
      prev.next = node.next
    node.value = None
    node.next = None

  def reverseOut(self):
    newLinked = LinkedList()
    node = self.head
    while(node != None):
      n = Node(node.value, None)
      if newLinked.head == None:
        newLinked.head = n
      else:
        n.next = newLinked.head
        newLinked.head = n
      node = node.next
    return newLinked

  def reverseIn(self):
    node = self.head
    newHead = None
    while(node != None):
      next = node.next
      node.next = newHead
      newHead = node
      node = next
    self.head = newHead

  def rotateLeft(self):
    node = self.head
    temp = None
    while (node != None):
      temp = node
      node = node.next

    old = self.head
    self.head = old.next
    temp.next = old
    old.next = None

  def rotateRight(self):
    node = self.head
    temp = None
    while(node != None):
      temp = node
      node = node.next

    temp.next = self.head
    self.head = temp

    temp = temp.next
    last = None
    while(temp != self.head):
      last = temp
      temp = temp.next

    last.next = None
# Tester Class
# list1 = [1, 2, 3, 4, 5]
# list2 = LinkedList()
# list2.convertlist(list1)
# list2.printList()
# list2.insertAtFirst(0)
# list2.printList()
# list2.insertAtEnd(6)
# list2.printList()
# list2.count()
# list2.get(list2.head, 3)
# print(list2.nodeAt(3))
# list2.get(list2.nodeAt(2), 3)
# list2.set(3, 3)
# list2.printList()
# print(list2.searchValue(3))
# list2.insertAt(4, 9)
# list2.printList()
# list2.insertAt(0, 9)
# list2.printList()
# list2.printList()
# list2.remove(0)
# list2.printList()
# list2.remove(2)
# list2.printList()
# c = Node('Karim', None)
# b = Node('Jalil', c)
# a = Node('Anushua', b)
# list3 = LinkedList()
# list3.head = a
# list3.tail = c
# list3.printList()
# list3.remove(1)
# list3.printList()
# list3.insertAt(1, 'Rifat')
# list3.printList()
# print(list3.tail)
# l = [1,2,3,4,5]
# list3.convertlist(l)
# list3.printList()
# print(list3.tail)
# makhlu = Node('maklu', None)
# n = list3.tail
# n.next = makhlu
# list3.printList()
# Test - 3
# li = [0, 1, 2, 3, 4, 5]
# linked = LinkedList()
# linked.convertlist(li)
# linked.printList()
# re = linked.reverseOut()
# re.printList()
# re.reverseIn()
# re.printList()
# re.rotateLeft()
# re.printList()