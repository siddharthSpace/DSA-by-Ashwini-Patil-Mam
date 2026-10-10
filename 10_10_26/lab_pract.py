# https://github.com/siddharthSpace/DSA-DayWise-Repo.git


class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.size=0
        self.head=None
    
    def append(self,data):
        newnode=Node(data)
        self.size+=1
        if not self.head:
            self.head=newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode

    def traverse(self):
        if not self.head:
            print("LL is empty")
            return
        print("List data:")
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
    
    def insertAtPos(self,data,pos):
        if pos<1 or pos>self.size or self.head==None:
            print("insertion not possible")
            return
        newnode=Node(data)
        tc=self.head
        tpre=tc
        c=0
        while c!=pos and tc.next!=None:
            tpre=tc
            tc=tc.next
            c+=1
        tpre.next=newnode
        newnode.next=tc
        self.size+=1

    def middleNode(self):
        mid = self.size // 2
        temp=self.head
        while mid!=0:
            temp = temp.next
            mid -= 1
        print("\nMid Node Val:",temp.data)

    def deleteAtPos(self,pos):
        if pos<1 or pos>self.size or self.head==None:
            print("list empty")
            return
        if pos==1:
            self.head=self.head.next
            self.size-=1
            return
        tc=self.head
        tpre=tc
        c=1
        while c<pos:
            tpre=tc
            tc=tc.next
            c+=1
        tpre.next=tc.next
        self.size-=1

    def reverseList(self):
        pre=None
        crnt=self.head
        while crnt:
            nextnode=crnt.next
            crnt.next=pre
            pre=crnt
            crnt=nextnode
        self.head=pre
        print("List reversed")

    def sum2Consecutive(self):
        if self.head==None or self.head.next==None:
            print("\nInsufficient no. of nodes")
            return
        print("\nSum of every 2 consecutive nodes:")
        temp = self.head
        while temp.next:
            print(temp.data + temp.next.data, end=" ")
            temp = temp.next

ml=SLL()

for i in range(1,7):
    ml.append(i)

ml.traverse()
ml.middleNode()
print("size:",ml.size)
ml.reverseList()
ml.traverse()
ml.sum2Consecutive()