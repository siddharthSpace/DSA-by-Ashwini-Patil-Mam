class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # Add to rear

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove from front
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Front ->", self.items, "<- Rear")


# --- Core DSA Algorithm ---
def reverse_queue(q):
    aux_stack = Stack()

    # Step 1: Dequeue all elements from Queue and Push onto Stack
    while not q.is_empty():
        element = q.dequeue()
        aux_stack.push(element)

    # Step 2: Pop all elements from Stack and Enqueue back into Queue
    while not aux_stack.is_empty():
        element = aux_stack.pop()
        q.enqueue(element)


# Driver Code
q = Queue()
for val in [10, 20, 30, 40]:
    q.enqueue(val)

print("Original Queue:")
q.display()  # Front -> [10, 20, 30, 40] <- Rear

reverse_queue(q)

print("Reversed Queue:")
q.display()  # Front -> [40, 30, 20, 10] <- Rear