# BST using Linked List

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    # Insert operation
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root

            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    # Inorder Traversal
    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.count += 1
            self.inorder(rt.right)

    # Preorder Traversal
    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    # Postorder Traversal
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")

    # Count nodes using recursion
    def countnodes(self, temp):
        if temp is None:
            return 0
        else:
            return (1 + self.countnodes(temp.left)
                    + self.countnodes(temp.right))

    # Count left subtree nodes
    def countleft(self):
        if self.root is None:
            print("Left nodes: 0")
        else:
            print("Left nodes:",
                  self.countnodes(self.root.left))

    # Count right subtree nodes
    def countright(self):
        if self.root is None:
            print("Right nodes: 0")
        else:
            print("Right nodes:",
                  self.countnodes(self.root.right))

    # Display left subtree
    def displayleft(self):
        print("Left Subtree:")
        if self.root is None or self.root.left is None:
            print("Empty")
        else:
            self.inorder(self.root.left)

    # Display right subtree
    def displayright(self):
        print("Right Subtree:")
        if self.root is None or self.root.right is None:
            print("Empty")
        else:
            self.inorder(self.root.right)

    # Find minimum and maximum
    def findminmax(self):
        if self.root is None:
            print("BST is empty")
            return

        temp = self.root

        while temp.left is not None:
            temp = temp.left

        print("\nMin:", temp.data)

        temp = self.root

        while temp.right is not None:
            temp = temp.right

        print("Max:", temp.data)


# Main program
b1 = BST()

b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))

print("\nInorder:")
b1.inorder(b1.root)

print("\nNo of nodes:", b1.count)

print("\nPreorder:")
b1.preorder(b1.root)

print("\nPostorder:")
b1.postorder(b1.root)

print("\nTotal nodes:", b1.countnodes(b1.root))

b1.countleft()
b1.countright()

b1.displayleft()
print()

b1.displayright()
print()

b1.findminmax()