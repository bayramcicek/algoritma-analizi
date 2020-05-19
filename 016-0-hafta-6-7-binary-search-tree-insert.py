#!/usr/bin/python3
# created by cicek on May 19, 2020 16:54

# kaynak: https://www.geeksforgeeks.org/binary-tree-set-1-introduction/
# Python program to introduce Binary Tree

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# # create root
# root = Node(1)
# ''' following is the tree after above statement
#         1
#       /   \
#      None  None'''
#
# root.left = Node(2);
# root.right = Node(3);
#
# ''' 2 and 3 become left and right children of 1
#            1
#          /   \
#         2      3
#      /    \    /  \
#    None None None None'''
#
# root.left.left = Node(4);
# '''4 becomes left child of 2
#            1
#        /       \
#       2          3
#     /   \       /  \
#    4    None  None  None
#   /  \
# None None'''

# A utility function to insert a new node with the given key
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


# Driver program to test the above functions
# Let us create the following BST
#      50
#    /      \
#   30     70
#   / \    / \
#  20 40  60 80

# A utility function to search a given key in BST
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root

        # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)

        # Key is smaller than root's key
    return search(root.left, key)


# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

# Print inoder traversal of the BST
inorder(r)

result = search(r, 20)
print("res = ", result.val)

'''
output:

20
30
40
50
60
70
80
res =  20

Process finished with exit code 0

'''
