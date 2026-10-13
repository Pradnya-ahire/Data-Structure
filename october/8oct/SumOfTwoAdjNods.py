
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def sum_consecutive(self):
        temp = self.head
        while temp and temp.next:
            print(temp.data + temp.next.data)
            temp = temp.next


lst = LinkedList()

lst.append(Node(10))
lst.append(Node(20))
lst.append(Node(30))
lst.append(Node(40))

print("Linked List:")
lst.print_list()

print("Sum of consecutive elements:")
lst.sum_consecutive()