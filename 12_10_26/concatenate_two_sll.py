
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

    def concatenate(self, second):
        if self.head is None:
            self.head = second.head
            return

        if second.head is None:
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = second.head

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


sll1 = SLL()
sll1.append(10)
sll1.append(20)
sll1.append(30)

sll2 = SLL()
sll2.append(40)
sll2.append(50)
sll2.append(60)

print("First SLL:")
sll1.display()

print("Second SLL:")
sll2.display()

sll1.concatenate(sll2)

print("After concatenation:")
sll1.display()
