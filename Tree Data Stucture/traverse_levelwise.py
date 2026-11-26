#Binary search tree
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class BST:
        def __init__(self):
            self.root = None

        def insert(self,newnode):
            if self.root is None: #creating the root node
                self.root = newnode
                
            else:
                temp = self.root
                while True:
                    if newnode.data<temp.data:
                        if temp.left is None:
                            temp.left = newnode
                            return
                        else:
                            temp = temp.left
                    elif newnode.data>= temp.data:
                        if temp.right is None:
                            temp.right = newnode
                            return
                        else:
                            temp = temp.right

        def level_order(self,rt):
            if rt is None:
                print("BST is empty")
                return

            arr = []
            cnt = 0 #for counting visited nodes

            arr.append(rt)
            while cnt < len(arr):
                temp=  arr[cnt]
                cnt += 1
                print(temp.data,end = " ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
    
              
def inorder(temp): # recursive
        if temp is None:
                return
        else:
            inorder(temp.left)
            print(temp.data,end = " ")
            inorder(temp.right)




b1 = BST()
b1.insert(Node(10))
b1.insert(Node(20))     
b1.insert(Node(6))     
b1.insert(Node(7))    
b1.insert(Node(25))    
b1.insert(Node(3))  
inorder(b1.root)   

print("\n:Level order:  ")
b1.level_order(b1.root)

