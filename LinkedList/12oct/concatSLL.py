class Node:
    def __init__(self,val):
        self.data = val
        self.next =None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,new_node):
        if self.head == None:
            self.head = new_node

        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node #Appending New Node

    def concat(self):
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = list1.head





    def print(self):
        temp = self.head
        print()
        print("linked list Elements: ")
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


list1  = LinkedList()
n1 = Node(100)
n2 = Node(200)
n3 = Node(300)
list1.append(n1)
list1.append(n2)
list1.append(n3)
list1.append(Node(400))

list1.print()


list.concat()
list.print()

