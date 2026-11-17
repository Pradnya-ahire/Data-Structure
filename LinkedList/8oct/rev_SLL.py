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

    def reverse(self):
        curr = self.head
        prev = None
        while(curr):
            nextnode = curr.next
            curr.next=prev
            prev = curr
            curr= nextnode
        self.head = prev



    def print(self):
        print("List Elements")
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

list1  = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list1.append(n1)
list1.append(n2)
list1.append(n3)
list1.append(Node(40))

list1.print()
print()
list1.reverse()
list1.print()



