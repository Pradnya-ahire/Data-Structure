

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def print(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

        


list = LinkedList()

list.insert_beginning(Node(30))
list.insert_beginning(Node(20))
list.insert_beginning(Node(10))

list.print()