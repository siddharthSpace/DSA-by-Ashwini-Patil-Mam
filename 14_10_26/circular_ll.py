# Circular Linked list 

# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def append(self, new_node):
#         if self.head==None:
#             new_node.next=self.head
#         else:
#             temp=self.head
#             while(temp.next!=self.head):
#                 temp = temp.next
#             temp.next=new_node
    
#     def insert(self , new_node , pos):
#         if pos == 1: # insert node at first position
#             new_node.next=self.head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

   
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")


    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return


        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        self.head = self.head.next
        temp.next = self.head


    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        # Only one node
        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head


cll = CircularLinkedList()

cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)

cll.display()

cll.insert_beginning(5)
cll.display()

cll.delete_beginning()
cll.display()

cll.delete_end()
cll.display()
