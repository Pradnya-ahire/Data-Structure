
# Hospital Emergency Management using Priority Queue


# Node class to create nodes
class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


# Hospital class
class Hospital:

    def __init__(self):
        self.front = None

    # Add Patient into queue(Enqueue)
    def enqueue(self):
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        priority = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        if priority < 1 or priority > 3:
            print("Invalid Priority!")
            return

        newnode = Node(pid, name, priority)

        if self.front is None or priority < self.front.priority:
            newnode.next = self.front
            self.front = newnode
        else:
            temp = self.front

            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next

            newnode.next = temp.next
            temp.next = newnode

        print("Patient added successfully!")

    # Display Next Patient
    def display_next(self):
        if self.front is None:
            print("No patients waiting!")
        else:
            print("\nNext Patient to be Treated:")
            print("Patient ID:", self.front.pid)
            print("Patient Name:", self.front.name)
            print("Priority:", self.front.priority)

    # Remove Patient (Dequeue)
    def dequeue(self):
        if self.front is None:
            print("No patients waiting!")
        else:
            temp = self.front
            print("Patient treated(Dequeue patient):", temp.name)
            self.front = self.front.next

    # Display All Patients
    def display_all(self):
        if self.front is None:
            print("No patients waiting!")
        else:
            print("\nWaiting Patients(patients in the list):")
            temp = self.front

            while temp is not None:
                print("Patient ID:", temp.pid)
                print("Patient Name:", temp.name)
                print("Priority:", temp.priority)
                print("----------------------")
                temp = temp.next


# Main Program
h = Hospital()

# Main Program
h = Hospital()

h.enqueue()
h.display_next()
h.display_all()
h.dequeue()
h.display_all()