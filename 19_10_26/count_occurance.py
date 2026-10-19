
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def count_occurrence(head, num):
    count = 0
    temp = head

    while temp is not None:
        if temp.data == num:
            count += 1

        temp = temp.next

    return count


# Creating a doubly linked list: 10 <-> 20 <-> 10 <-> 30 <-> 10
n1 = Node(10)
n2 = Node(20)
n3 = Node(10)
n4 = Node(30)
n5 = Node(10)

n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3
n4.next = n5
n5.prev = n4

head = n1

num = 10
print("Occurrence:", count_occurrence(head, num))
