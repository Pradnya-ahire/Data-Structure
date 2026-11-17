class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self,val):
        newnode = Node(val)
        if self.head == None:
            self.head = newnode
            return
        temp = self.head
        while temp.next != None:
            temp= temp.next
        temp.next = newnode

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end = "-> ")
            temp=temp.next
        print("None")

    def insert(self,val,pos):
        if pos<0:
            print("Inavlid Position")
            return
        
        if pos == 1:
            self.head = newnode
            return
        
        temp = self.head
        for i in range(pos-2):
            if temp is None:
                print("Invalid")
                return
        temp = temp.next

        if temp is None:
            print("invalid")
            return
        
        newnode = Node(val)
        newnode.next=temp.next
        temp.next = newnode


    def delete_neg(self):
        temp = self.head
        prev = None

        while temp is not None:
            if temp.data<0:
                if prev == None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
            else:
                prev = temp
            temp = temp.next


        





l1=LinkedList()
l1.append(20)
l1.append(-34)
l1.append(-40)
l1.append(30)

l1.print()

l1.insert(23,3)
l1.print()

l1.delete_neg()
l1.print()
























































# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.next = None
 
# class LinkedList:
#     def __init__(self):
#         self.head = None
 
#     def append(self, val):
#         new_node = Node(val)
#         if self.head is None:
#             self.head = new_node
#             return
#         temp = self.head
#         while temp.next is not None:
#             temp = temp.next
#         temp.next = new_node
 
#     def display(self):
#         temp = self.head
#         while temp is not None: 
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")
 
#     def insert_beginning(self, val):
#         new_node = Node(val)
#         new_node.next = self.head
#         self.head = new_node
 
#     def insert_position(self, val, pos):
#         if pos < 1:
#             print("Invalid position")
#             return
#         if pos == 1:
#             self.insert_beginning(val)
#             return
#         temp = self.head
#         for i in range(pos - 2):
#             if temp is None:
#                 print("Invalid position")
#                 return
#             temp = temp.next
#         if temp is None:
#             print("Invalid position")
#             return
#         new_node = Node(val)
#         new_node.next = temp.next
#         temp.next = new_node
 
#     def delete_value(self, val):
#         if self.head is None:
#             print("List is empty")
#             return
#         if self.head.data == val:
#             self.head = self.head.next
#             return
#         temp = self.head
#         while temp.next is not None:
#             if temp.next.data == val:
#                 temp.next = temp.next.next
#                 return
#             temp = temp.next
#         print("Value not found")
 
#     def search(self, val):
#         temp = self.head
#         pos = 1
#         while temp is not None:
#             if temp.data == val:
#                 print("Found at position", pos)
#                 return
#             temp = temp.next
#             pos += 1
#         print("Value not found")
 
#     def count_nodes(self):
#         temp = self.head
#         count = 0
#         while temp is not None:
#             count += 1
#             temp = temp.next
#         print("Total nodes:", count)
 
#     def sum_nodes(self):
#         temp = self.head
#         total = 0
#         while temp is not None:
#             total += temp.data
#             temp = temp.next
#         print("Sum:", total)
 
#     def reverse(self):
#         prev = None
#         curr = self.head
#         while curr is not None:
#             nextnode = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nextnode
#         self.head = prev
 
#     def find_middle(self):
#         if self.head is None:
#             print("List is empty")
#             return
#         slow = self.head
#         fast = self.head
#         while fast is not None and fast.next is not None:
#             slow = slow.next
#             fast = fast.next.next
#         print("Middle node:", slow.data)
 
#     def print_alternate(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.data, end=" ")
#             temp = temp.next
#             if temp is not None:
#                 temp = temp.next
#         print()
 
# ll = LinkedList()
# ll.append(10)
# ll.append(20)
# ll.append(30)
# ll.append(40)
# ll.append(50)
 
# print("Original list:")
# ll.display()
# ll.insert_beginning(5)
# print("After insertion:")
# ll.display()
# ll.insert_position(25, 3)
# ll.display()
# ll.search(30)
# ll.count_nodes()
# ll.sum_nodes()
# ll.find_middle()
# ll.print_alternate()
# ll.delete_value(25)
# ll.display()
# ll.reverse()
# print("Reversed list:")
# ll.display()
