# write a function to print node values in reverse order in the doubly linear linked list 

# def display_reverse(head):
#     if head is None:
#         return

#     temp = head

#     # Move to the last node
#     while temp.next is not None:
#         temp = temp.next

#     # Print nodes in reverse order
#     while temp is not None:
#         print(temp.data, end=" ")
#         temp = temp.prev



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

    def display_reverse(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        # Move to the last node
        while temp.next is not None:
            temp = temp.next

        # Print in reverse order
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.prev


dll = DoublyLinkedList()

dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_end(40)

print("Reverse order:")
dll.display_reverse()
