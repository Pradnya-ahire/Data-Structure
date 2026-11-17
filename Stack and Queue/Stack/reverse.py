class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
        def __init__(self):
            self.top= None
        def isempty(self):
            return self.top is None
        def push(self,newnode):
            newnode.next = self.top
            self.top = newnode

        def pop(self):
             temp=self.top
             if self.isempty():
                print("Stack is Empty")

             else:
                 print("\nPoped Element: ",temp.data)
                 self.top=self.top.next
                 temp=None

        def reverse(self):
            temp = self.top 

            while temp:
                st1.push(Node(temp.data))
                temp = temp.next


        def print(self):
            if self.isempty():
                print("Stack is Empty\n")
            else:
                print("Stack contains....")
                temp = self.top
                while temp :
                    print(temp.data)
                    temp=temp.next
                

st1 = Stack()
st = Stack()

st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))

st.print()

st.pop()

print("\nReversed stack")
st.reverse()
st1.print()



