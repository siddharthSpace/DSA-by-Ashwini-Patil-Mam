
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def swap_first_last(head):
    if head is None or head.next is None:
        return head

    first = head
    last = head

    while last.next is not None:
        last = last.next

    first.data, last.data = last.data, first.data

    return head


def display(head):
    temp = head

    while temp is not None:
        print(temp.data, end=" <-> ")
        temp = temp.next

    print("None")


# Creating DLL: 10 <-> 20 <-> 30 <-> 40
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3

head = n1

print("Before swapping:")
display(head)

head = swap_first_last(head)

print("After swapping:")
display(head)
