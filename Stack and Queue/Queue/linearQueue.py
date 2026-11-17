class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class linearQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,newnode):
        if self.rear:
            self.rear.next = newnode
            self.rear=newnode

        else:
            self.front =self.rear=newnode
    def dequeue(self):

        temp = self.front
        print("\nDeteled Node: ",temp.data)
        self.front=self.front.next

        if self.front == None:
            self.rear = None
            print("Queue is Emplty Now...")
            self.rear = None

        temp = None

    def print(self):
        temp = self.front 
        while temp :
            print(temp.data,end  = "->")
            temp= temp.next
        print(None)


Q = linearQueue()
Q.enqueue(Node(230))
Q.enqueue(Node(400))
Q.enqueue(Node(223))
Q.enqueue(Node(132))
Q.enqueue(Node(231))

Q.print()

Q.dequeue()
Q.print()

Q.dequeue()
Q.print()

Q.dequeue()
Q.print()

Q.dequeue()
Q.print()

Q.dequeue()
Q.print()