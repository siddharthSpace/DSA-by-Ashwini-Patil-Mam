# Singly Linear Linked List: deletion by value


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
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, value):
        if self.head is None:
            return False

        # Handle deletion of the first node.
        if self.head.data == value:
            self.head = self.head.next
            return True

        previous = self.head
        current = self.head.next

        while current:
            if current.data == value:
                previous.next = current.next
                return True
            previous = current
            current = current.next

        return False  # The value was not found.

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

if linked_list.delete(20):
    print("Node deleted")
else:
    print("Value not found")

linked_list.print()
