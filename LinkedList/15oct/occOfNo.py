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

    def count_occ(self,num):
           temp = self.head
           cnt = 0
           while(temp):
               if temp.data == num:
                    cnt += 1
               temp = temp.next
           print("Occurence of number is : ",cnt)
           

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
list.append(Node(40))
list.append(Node(40))


list.print()
list.count_occ(40)
list.print()




