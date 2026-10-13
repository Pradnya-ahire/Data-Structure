# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
        
#         self.head = None
        

#     def append(self,new_node):

#         if self.head == None:
#             self.head = new_node

#         else:
#             temp = self.head
#             while temp.next is not None:
#                 temp = temp.next
#             temp.next = new_node

#     def sum(self):
#         temp = self.head
#         sum =0 
#         while temp.next != None:
#             sum = temp.data +temp.next.data
#             temp = temp.next

#         print("Sum of elements: ",sum)


    

#     def print(self):
#         temp = self.head
#         while temp:
#             print(temp.data,end ="->")
#             temp = temp.next

#         print(None)

# l1 = LinkedList()
# n1 = Node(10)
# n2 =Node(20)

# l1.append(n1)
# l1.append(n2)
# l1.print()
# l1.sum()



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     # 1. Create linked list
#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         temp = self.head
#         while temp.next is not None:
#             temp = temp.next

#         temp.next = new_node

#     # 2. Traverse and print
#     def display(self):
#         if self.head is None:
#             print("Linked List is empty")
#             return

#         temp = self.head
#         while temp is not None:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")

#     # 3. Insert at a specific position (1-based)
#     def insert(self, data, pos):
#         if pos < 1:
#             print("Invalid position")
#             return

#         new_node = Node(data)

#         if pos == 1:
#             new_node.next = self.head
#             self.head = new_node
#             return

#         temp = self.head
#         count = 1

#         while temp is not None and count < pos - 1:
#             temp = temp.next
#             count += 1

#         if temp is None:
#             print("Invalid position")
#             return

#         new_node.next = temp.next
#         temp.next = new_node

#     # 4. Find middle node
#     def middle(self):
#         if self.head is None:
#             print("Linked List is empty")
#             return

#         slow = self.head
#         fast = self.head

#         while fast is not None and fast.next is not None:
#             slow = slow.next
#             fast = fast.next.next

#         print("Middle node:", slow.data)

#     # 5. Delete node at a specific position
#     def delete(self, pos):
#         if pos < 1 or self.head is None:
#             print("Invalid position")
#             return

#         if pos == 1:
#             self.head = self.head.next
#             return

#         temp = self.head
#         count = 1

#         while temp.next is not None and count < pos - 1:
#             temp = temp.next
#             count += 1

#         if temp.next is None:
#             print("Invalid position")
#             return

#         temp.next = temp.next.next

#     # 6. Reverse linked list
#     def reverse(self):
#         prev = None
#         current = self.head

#         while current is not None:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node

#         self.head = prev

#     # 7. Sum of every two consecutive nodes
#     def consecutive_sum(self):
#         if self.head is None or self.head.next is None:
#             print("Need at least two nodes")
#             return

#         temp = self.head

#         while temp is not None and temp.next is not None:
#             total = temp.data + temp.next.data
#             print(temp.data, "+", temp.next.data, "=", total)
#             temp = temp.next


# # Main program
# ll = LinkedList()

# n = int(input("Enter number of nodes: "))

# for i in range(n):
#     value = int(input("Enter node value: "))
#     ll.append(value)

# print("\nOriginal Linked List:")
# ll.display()

# data = int(input("\nEnter value to insert: "))
# pos = int(input("Enter position to insert: "))
# ll.insert(data, pos)
# ll.display()

# ll.middle()

# pos = int(input("\nEnter position to delete: "))
# ll.delete(pos)
# ll.display()

# ll.reverse()
# print("\nReversed Linked List:")
# ll.display()

# print("\nConsecutive Pair Sums:")
# ll.consecutive_sum()



class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create linked list
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    # 2. Traverse and print
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print(None)

    # 3. Insert node at any position
    def insert(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return

        new_node = Node(data)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(pos - 2):
            if temp == None:
                print("Invalid position")
                return
            temp = temp.next

        if temp == None:
            print("Invalid position")
            return

        new_node.next = temp.next              
        temp.next = new_node

    # 4. Find middle node
    def middle(self):
        temp = self.head
        count = 0

        while temp:
            count = count + 1
            temp = temp.next

        if count == 0:
            print("List is empty")
            return

        temp = self.head
        for i in range(count // 2):
            temp = temp.next

        print("Middle node:", temp.data)

    # 5. Delete node by value
    def del_node(self, value):
        temp = self.head

        if temp == None:
            print("List is empty")
            return

        if temp.data == value:
            self.head = self.head.next
            return

        prev = temp
        temp = temp.next

        while temp:
            if temp.data == value:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

        print("Value is not present")

    # 6. Reverse linked list
    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        self.head = prev

    # 7. Sum of two consecutive nodes
    def sum_consecutive(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data, "+", temp.next.data, "=",
                  temp.data + temp.next.data)
            temp = temp.next


# Main program
lst = LinkedList()

lst.append(Node(10))
lst.append(Node(20))
lst.append(Node(30))
lst.append(Node(40))
lst.append(Node(50))

print("Original Linked List:")
lst.print()

print("\nInsert 25 at position 3:")
lst.insert(25, 3)
lst.print()

print("\nMiddle node:")
lst.middle()

print("\nDelete node with value 20:")
lst.del_node(20)
lst.print()

print("\nReverse Linked List:")
lst.reverse()
lst.print()

print("\nSum of consecutive nodes:")
lst.sum_consecutive()
