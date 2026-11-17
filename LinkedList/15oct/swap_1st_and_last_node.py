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
    def Swap_first_last(self):
        temp=node1=self.head # node1 1 is first node
        while(temp.next):  # temp is last node
            temp = temp.next
        
        
        temp.next=node1.next
        node1.next=None
        node1.prev= temp.next
        temp.prev.next=node1
        temp.prev = None
        self.head=temp


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

list.print()
list.Swap_first_last()


list.print()

