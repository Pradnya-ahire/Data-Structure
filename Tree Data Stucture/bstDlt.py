#Binary search tree
#dlt cases--->1.leaf node  2.node with right child   3.node with only left child node with left and right children 
# 
# 4.node with both chilren
# class Node:
#     def __init__(self,val):
#         self.data = val
#         self.left = None
#         self.right = None

# class BST:
#         def __init__(self):
#             self.root = None

#         def insert(self,newnode):
#             if self.root is None: #creating the root node
#                 self.root = newnode
                
#             else:
#                 temp = self.root
#                 while True:
#                     if newnode.data<temp.data:
#                         if temp.left is None:
#                             temp.left = newnode
#                             return
#                         else:
#                             temp = temp.left
#                     elif newnode.data>= temp.data:
#                         if temp.right is None:
#                             temp.right = newnode
#                             return
#                         else:
#                             temp = temp.right

# def inorder(temp): # recursive
#         if temp is None:
#                 return
#         else:
#                 inorder(temp.left)
#                 print(temp.data,end = " ")
#                 inorder(temp.right)

# def preorder(temp): # recursive
#         if temp is None:
#                 return
#         else:
#                 print(temp.data,end = " ")
#                 inorder(temp.left)
#                 inorder(temp.right)

# def postorder(temp): # recursive
#         if temp is None:
#                 return
#         else:
#                 inorder(temp.left)
#                 inorder(temp.right)
#                 print(temp.data,end = " ")


# def del_node(self, rt, val):
#     if rt is None:
#             return rt
#     if val < rt.data:
#           rt.left = self.del_noe(rt.left,val)
#     elif val >rt.data:
#           rt.right = self.dlt_node(rt.right,val)
#     else:
#           if rt.left is None:  #Node with right child only 
#                 return rt.right
#           if rt.right is None:  #node with left child only
#                 return rt.left    

#           #node has both left and right childrens
#           succ = self.get_successor(rt)
#           rt.data=succ.data
#           rt.right = self.del_node(rt.right,succ.data)
#     return rt

# def get_successor(self,temp):
#       temp= temp.right
#       while temp.left is not None :
#             temp= temp.left
#       return temp
            
      
      

# b1 = BST()
# b1.insert(Node(10))
# b1.insert(Node(20))     
# b1.insert(Node(6))     
# b1.insert(Node(7))    
# b1.insert(Node(25))    
# b1.insert(Node(3))  

# print("\nInoder traversal:")
# inorder(b1.root)  

# print("\npreoreder traversal:")
# preorder(b1.root) 

# print("\npostorder traversal:")
# postorder(b1.root) 

# b1.del_node(b1.root,3)
# print("\nAfter Deletion: ",end = " " )
# b1.inorder(b1.root)






# Binary Search Tree - Deletion

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, newnode):
        if self.root is None:
            self.root = newnode
        else:
            temp = self.root
            while True:
                if newnode.data < temp.data:
                    if temp.left is None:
                        temp.left = newnode
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = newnode
                        return
                    else:
                        temp = temp.right

    # Inorder
    def inorder(self, temp):
        if temp is None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data, end=" ")
            self.inorder(temp.right)

    # Preorder
    def preorder(self, temp):
        if temp is None:
            return
        else:
            print(temp.data, end=" ")
            self.preorder(temp.left)
            self.preorder(temp.right)

    # Postorder
    def postorder(self, temp):
        if temp is None:
            return
        else:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data, end=" ")

    # Find Inorder Successor
    def get_successor(self, temp):
        temp = temp.right
        while temp.left is not None:
            temp = temp.left
        return temp

    # Delete Node
    def del_node(self, rt, val):

        if rt is None:
            return rt

        if val < rt.data:
            rt.left = self.del_node(rt.left, val)

        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)

        else:

            # Case 1 and 2: No left child
            if rt.left is None:
                return rt.right

            # Case 3: No right child
            if rt.right is None:
                return rt.left

            # Case 4: Both children present
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right, succ.data)

        return rt
    def search(self,key):
        temp = self.root
        while temp:
            if temp.data==key:
                return True
            elif key < temp.data:
                temp = temp.left
            elif key > temp.data:
                temp = temp.right


# Main program

b1 = BST()

b1.insert(Node(10))
b1.insert(Node(20))
b1.insert(Node(6))
b1.insert(Node(7))
b1.insert(Node(25))
b1.insert(Node(3))

print("\nInorder traversal:")
b1.inorder(b1.root)

print("\nPreorder traversal:")
b1.preorder(b1.root)

print("\nPostorder traversal:")
b1.postorder(b1.root)

# Delete node
b1.del_node(b1.root, 3)

print("\nAfter deletion:")
b1.inorder(b1.root)

if b1.search(25):
    print("\nFound the node!!!")
else:
    print("\nNot Found")