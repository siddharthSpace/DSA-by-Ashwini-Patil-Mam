# Singly Linear Linked List

class Node:
  def __init__(self, val):
    self.data = val
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, new_node, pos):
    """Insert new_node at zero-based position pos."""
    if pos < 0:
      raise IndexError("position must be non-negative")

    if pos == 0:
      new_node.next = self.head
      self.head = new_node
      return

    temp = self.head
    for _ in range(pos - 1):
      if temp is None:
        raise IndexError("position is out of range")
      temp = temp.next

    if temp is None:
      raise IndexError("position is out of range")
    new_node.next = temp.next
    temp.next = new_node

  def append(self, new_node):
    if (self.head == None):
      self.head = new_node
    else:
      temp = self.head
      while(temp.next):
        temp = temp.next
      temp.next = new_node  # appending new node

  def print(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next

list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.print()
 