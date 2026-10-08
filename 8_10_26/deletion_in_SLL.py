# Singly Linear Linked List

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete(self, value):
        if self.head is None:
            return False

        # Delete the head node if it matches
        if self.head.data == value:
            self.head = self.head.next
            return True

        # Find the node and link around it
        previous = self.head
        current = self.head.next

        while current:
            if current.data == value:
                previous.next = current.next
                return True
            previous = current
            current = current.next

        return False  # Value was not found

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


linked_list = LinkedList()

linked_list.append(Node(10))
linked_list.append(Node(20))
linked_list.append(Node(30))
linked_list.append(Node(40))

linked_list.delete(20)

linked_list.print()