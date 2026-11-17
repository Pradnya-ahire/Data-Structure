
# Priority Queue Implementation

class PriorityQueue:

    def __init__(self):
        self.queue = []

    # Insert element into queue
    def enqueue(self):
        data = int(input("Enter data: "))
        priority = int(input("Enter priority: "))

        self.queue.append([data, priority])

        # Sort according to priority
        self.queue.sort(key=lambda x: x[1])

        print("Element inserted successfully!")

    # Remove element from queue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is Empty!")
        else:
            item = self.queue.pop(0)
            print("Deleted Element:", item[0])

    # Display queue
    def display(self):
        if len(self.queue) == 0:
            print("Queue is Empty!")
        else:
            print("Priority Queue:")
            for item in self.queue:
                print("Data:", item[0], "Priority:", item[1])

# Main Program
q = PriorityQueue()

while True:
    print("\n--- Priority Queue ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        q.enqueue()
    elif ch == 2:
        q.dequeue()
    elif ch == 3:
        q.display()
    elif ch == 4:
        print("Exit")
        break
    else:
        print("Invalid Choice!")