class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
    
    class LQueue:
        def __init__(self):
            self.front=self.rear=None
        def enqueue(self, new_node):
            if self.rear:
                self.rear.next=new_node
                self.rear=new_node
            
            else:
                self.front=self.rear=new_node

que=LQueue()
que.enqueue(Node(23))
que.enqueue(Node(63))
que.enqueue(Node(78))
que.enqueue(Node(20))


    
