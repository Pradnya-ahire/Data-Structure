class Node:
    def __init__(self,val):
        self.data = val
        self.next =None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,new_node):
        temp = self.head
        if temp:
            while temp.next:
                temp = temp.next #finding last node
            temp.next=new_node
            new_node.prev=temp

        else: #only to add first node
           self.head=new_node


    def insert(self,new_node,pos):
        temp = self.head
        if pos==1:
            new_node.next=self.head
            self.head.prev = new_node
            self.head=new_node
            return
        else:
            p=1
            while (p!=pos-1):
                temp=temp.next
                p+=1
            new_node.next=temp.next                
            temp.next=new_node
            new_node.prev=temp
           

            if temp.next: #Last Position
                temp.next.prev=new_node
            return






    def print(self):
        temp = self.head
        while(temp):
            print(temp.data,end = "->")
            temp = temp.next
        print(None)

list  = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))

list.print()
list.insert(Node(70),3)
list.print()



