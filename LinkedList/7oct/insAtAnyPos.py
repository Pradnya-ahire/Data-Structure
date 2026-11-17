
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

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
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

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

print("Original list:")
ll.display()

ll.insert(25, 3)
print("After insertion:")
ll.display()

ll.insert(50, 10)
