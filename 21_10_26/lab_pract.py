class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
       new = Node(data)

       
       if self.head is None:
            self.head = new
       else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
    
    def display(self):
        temp= self.head
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")

    def insert(self, data , pos):
        new= Node(data)

        if pos ==1:
            new.next = self.head
            self.head=new
            return

        temp = self.head
        for i in range(pos - 2):
            if temp is None:
                print("Invalid Pos")
                return
            temp = temp.next

        if temp is None:
            print("Invalid Pos")
            return

        new.next=temp.next
        temp.next=new

    def delete(self):
        while self.head and self.head.data < 0:
            self.head = self.head.next
        
        temp = self.head
        while temp and temp.next:
            if temp.next.data < 0:
                temp.next=temp.next.next
            else:
                temp=temp.next


s = LinkedList()

n = int(input("enter no of node:"))

for i in range(n):
    x= int(input("enter value:"))
    s.append(x)

print("Original list:")
s.display()

x= int(input("enter value to insert:"))
p= int(input("enter position"))
s.insert(x , p)

print("after insertion")
s.display()

s.delete()
print("after deleting negative node;")
s.display()