# class LinkedList:
#     def reverse(self): #Reversing a linked list
#         self.head=prev
#     def findmid_del(self):
#         temp=temp1=self.head
#         prev=None
#         while temp1 and temp1.next:
#             prev=temp
#             temp=temp1.next.next
#         print("Middle Node:", temp.data)
#         prev.next=temp.next
#         temp=None
#     def delfirst_last(self):
#         temp1=self.head

# write a function to delete first & last node in SLL


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class SLL:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         newnode = Node(data)

#         if self.head is None:
#             self.head = newnode
#             return

#         temp = self.head

#         while temp.next:
#             temp = temp.next

#         temp.next = newnode

#     # 1. Delete from beginning
#     def delete_beginning(self):
#         if self.head is None:
#             print("List is empty")
#             return

#         self.head = self.head.next

#     # 2. Delete from end
#     def delete_end(self):
#         if self.head is None:
#             print("List is empty")
#             return

#         if self.head.next is None:
#             self.head = None
#             return

#         temp = self.head

#         while temp.next.next:
#             temp = temp.next

#         temp.next = None

#     # 3. Delete from a specific position
#     # Positions start from 1
#     def delete_position(self, position):
#         if self.head is None:
#             print("List is empty")
#             return

#         if position < 1:
#             print("Invalid position")
#             return

#         if position == 1:
#             self.head = self.head.next
#             return

#         temp = self.head

#         for i in range(position - 2):
#             if temp.next is None:
#                 print("Position out of range")
#                 return
#             temp = temp.next

#         if temp.next is None:
#             print("Position out of range")
#             return

#         temp.next = temp.next.next

#     def display(self):
#         temp = self.head

#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next

#         print("None")


# # Main program
# sll = SLL()

# sll.append(10)
# sll.append(20)
# sll.append(30)
# sll.append(40)

# print("Original list:")
# sll.display()

# sll.delete_position(3)

# print("After deleting position 3:")
# sll.display()



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newnode

    # Delete the first node
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # Delete the last node
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        # If there is only one node
        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        # Reach the second-last node
        while temp.next.next:
            temp = temp.next

        temp.next = None

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
sll = SLL()

sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)

print("Original list:")
sll.display()

sll.delete_first()
print("After deleting first node:")
sll.display()

sll.delete_last()
print("After deleting last node:")
sll.display()