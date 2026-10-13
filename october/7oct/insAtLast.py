class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_last(self, new_node):

        # If linked list is empty
        if self.head is None:
            self.head = new_node
            return

        # Start from head
        temp = self.head

        # Go to last node
        while temp.next is not None:
            temp = temp.next

        # Add new node at last
        temp.next = new_node

    def print(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

        


# Create linked list
list = LinkedList()

list.insert_last(Node(10))
list.insert_last(Node(20))
list.insert_last(Node(30))
list.insert_last(Node(40))

list.print()