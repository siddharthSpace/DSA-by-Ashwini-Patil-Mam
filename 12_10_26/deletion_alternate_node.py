
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

    def delete_alternate(self):
        temp = self.head

        while temp and temp.next:
            temp.next = temp.next.next
            temp = temp.next

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


sll = SLL()

sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)

print("Original list:")
sll.display()

sll.delete_alternate()

print("After deleting alternate nodes:")
sll.display()
