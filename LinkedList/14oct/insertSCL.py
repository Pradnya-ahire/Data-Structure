
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node, pos):


        if pos == 1:
            temp= self.head
            while(temp.next!=self.head):
                temp= temp.next
            new_node.next=self.head
            self.head = new_node
            temp.next=self.head

        else:
            p=1
            temp = self.head
            while(p!=pos-1):
                temp = temp.next
                p+=1
            new_node.next=temp.next
            temp.next=new_node

    def delete(self,value):
        temp = self.head
        prev = None
        if temp.dta==value:
            while(temp.next!=self.head):
                temp = temp.next
            self.head = self.head.next
            temp.next=self.next

        else:
            while(temp.data!=value and temp):
                prev = temp
                temp = temp.next
                if temp == None:
                    print("value ios present in the list")
                    return
                prev.next=temp.next
                temp = None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 



        

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


ll = LinkedList()

ll.insert(10, 1)
ll.insert(20, 2)
ll.insert(30, 3)
ll.insert(40, 4)
ll.insert(50, 5)


print("Original list:")
ll.display()

ll.insert(25, 3)
print("After insertion:")
ll.display()

ll.insert(50, 10)
ll.insert(56, 4)
ll.display()


