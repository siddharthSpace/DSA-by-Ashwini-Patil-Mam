# W.A.P to reverse stack elements using queue.
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self, new_node):
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.top is None:
            return None
        temp=self.top
        self.top=self.top.next
        return temp.data
    def print(self):
        temp=self.top
        print("Stack Elements:")
        while temp:
            print(temp.data, end=" -> ")
            temp=temp.next
        print("None")
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front is None
    def enqueue(self, data):
        new = Node(data)
        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            self.rear = new
    def dequeue(self):
        if self.front:
            temp=self.front
            data=temp.data
            self.front=self.front.next
            if self.front is None:
                self.rear=None
            return data
        else:
            return None
    def print_queue(self):
        curr=self.front
        print("Queue Elements:")
        while curr is not None:
            print(curr.data, end=" -> ")
            curr=curr.next
        print("None")
def reverse_stack(st1):
    q1=Queue()
    # Transfer Stack to Queue
    while st1.top is not None:
        q1.enqueue(st1.pop())
    q1.print_queue()
    # Transfer Queue back to Stack
    while not q1.is_empty():
        st1.push(Node(q1.dequeue()))
# Main program
st=Stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
print("Original Stack:")
st.print()
reverse_stack(st)
print("\nReversed Stack:")
st.print()