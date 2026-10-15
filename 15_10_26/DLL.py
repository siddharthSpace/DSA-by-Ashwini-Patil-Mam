# Doubly Linear Linked List.

# class Node:
#   def __init__(self,value):
#     self.data = value
#     self.next = None

# class LinkedList:
#   def __init__(self):
#     self.head = None

#   def append(self,new_node):
#     temp = self.head
#     if temp:
#       while temp.next:
#         temp = temp.next
#       temp.next = new_node
#       new_node.prev = temp
#     else:  # First Node
#       self.head = new_node

#   def insert(self,new_node,pos):
#     temp = self.head 
#     if pos == 1:
#       new_node.next = self.head
#       self.head.prev = new_node
#       self.head = new_node
#     else:
           

#   def print(self):  
#     temp = self.head
#     print("List elements : ",end=" ")
#     while temp:
#       print(temp.data,end=" ")
#       temp = temp.next  

# list1 = LinkedList()
# list1.append(Node(12))
# list1.append(Node(52))
# list1.append(Node(102))
# list1.append(Node(56))   
# print()


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    def display_backward(self):
        temp = self.head

        if temp is None:
            return

        while temp.next is not None:
            temp = temp.next

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


dll = DoublyLinkedList()

dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)

print("Forward:")
dll.display_forward()

print("Backward:")
dll.display_backward()
