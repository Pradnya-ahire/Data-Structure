# class Stack:

#     def __init__(self):
#         self.stack = []

#     def push(self):
#         x = input("Enter element: ")
#         self.stack.append(x)
#         print("Element pushed")

#     def pop(self):
#         if len(self.stack) == 0:
#             print("Stack is Empty")
#         else:
#             print("Popped element:", self.stack.pop())

#     def display(self):
#         print("Stack:", self.stack)

#     def reverse_string(self):
#         s = input("Enter string: ")
#         temp = []

#         for i in s:
#             temp.append(i)

#         rev = ""
#         while len(temp) > 0:
#             rev = rev + temp.pop()

#         print("Reversed String:", rev)

#     def reverse_stack(self):
#         temp = []

#         while len(self.stack) > 0:
#             temp.append(self.stack.pop())

#         while len(temp) > 0:
#             self.stack.append(temp.pop())

#         print("Reversed Stack:", self.stack)


# # Main Program
# s = Stack()

# s.push()
# s.push()
# s.display()
# s.pop()
# s.display()
# s.reverse_string()
# s.reverse_stack()
# s.display()


# Program to perform Linear Queue operations using Class

class Queue:

    # Constructor to create an empty queue
    def __init__(self):
        self.queue = []

    # Function to insert an element into queue
    def enqueue(self):
        x = input("Enter element: ")
        self.queue.append(x)
        print("Element inserted successfully")

    # Function to delete an element from queue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print("Deleted element:", self.queue.pop(0))

    # Function to display queue elements
    def display(self):
        print("Queue Elements:", self.queue)

    # Function to reverse queue using stack
    def reverse_queue(self):
        stack = []

        # Move queue elements into stack
        while len(self.queue) > 0:
            stack.append(self.queue.pop(0))

        # Move elements back from stack to queue
        while len(stack) > 0:
            self.queue.append(stack.pop())

        print("Reversed Queue:", self.queue)

    # Function to merge two queues
    def merge_queue(self, q2):
        self.queue = self.queue + q2.queue
        print("Merged Queue:", self.queue)

    # Function to check whether two queues are identical
    def identical(self, q2):
        if self.queue == q2.queue:
            print("Queues are Identical")
        else:
            print("Queues are Not Identical")


# Main Program: Create two queue objects
q1 = Queue()
q2 = Queue()

# Insert elements into first queue
print("Enter First Queue:")
q1.enqueue()
q1.enqueue()
q1.display()

# Insert elements into second queue
print("Enter Second Queue:")
q2.enqueue()
q2.enqueue()
q2.display()

# Delete an element from first queue
q1.dequeue()

# Display first queue
q1.display()

# Reverse first queue using stack
q1.reverse_queue()

# Check whether two queues are identical
q1.identical(q2)

# Merge both queues
q1.merge_queue(q2)