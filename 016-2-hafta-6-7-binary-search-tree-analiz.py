#!/usr/bin/python3
# created by cicek on May 19, 2020 17:34

import math, random

# binary search tree deneysel analizi

'''
n = düğüm sayısı
log ((2^k+1) - 1) = log(N)
k = log(n) -> yaklaşık

best case = 1
worst case = n
'''


class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.depth = 0  # ağacın o anki derinliği

    def __str__(self):
        return "val: " + str(self.val) + "depth: " + str(self.depth)


def insert(root, node):
    if root is None:
        root = node
    else:
        node.depth += 1
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
sumOfDepth = 0
numOfNodes = 0


def inorder(root):
    global sumOfDepth
    global numOfNodes
    if root:
        inorder(root.left)
        print(root.val, root.depth, end=" -- ")

        sumOfDepth += root.depth
        numOfNodes += 1

        inorder(root.right)


r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

for i in range(100):
    rand = random.randint(-1000, 1000)
    insert(r, Node(rand))

# Print inoder traversal of the BST
inorder(r)
print("\n", sumOfDepth, numOfNodes, sumOfDepth/numOfNodes, math.log(numOfNodes))
# sumOfDepth/numOfNodes -> ortalama derinlik değeri - deneysel değer
# deneysel değer ve log(n) değeri birbirine yakın

'''
output:

-999 4 -- -994 6 -- -979 7 -- -930 5 -- -874 3 -- -867 8 -- -851 7 -- -817 8
-- -810 6 -- -781 10 -- -726 9 -- -725 8 -- -700 9 -- -692 10 -- -670 11 -- -635 12
-- -577 7 -- -541 5 -- -537 8 -- -535 9 -- -533 7 -- -523 8 -- -506 9 -- -493 6 -- -477 8
-- -464 9 -- -446 7 -- -438 9 -- -434 10 -- -385 8 -- -376 10 -- -364 11 -- -325 9 -- -318 4
-- -304 8 -- -299 9 -- -293 7 -- -255 6 -- -236 10 -- -226 9 -- -211 10 -- -198 11 -- -185 13
-- -185 12 -- -184 8 -- -174 7 -- -146 9 -- -124 10 -- -115 8 -- -112 9 -- -99 10 -- -87 5
-- -65 7 -- -61 6 -- -32 8 -- 2 7 -- 20 2 -- 30 1 -- 36 3 -- 37 4 -- 40 5 -- 40 2 -- 50 0
-- 60 3 -- 60 2 -- 70 1 -- 80 2 -- 108 6 -- 147 7 -- 153 5 -- 157 7 -- 187 8 -- 215 6 -- 219 9
-- 250 10 -- 262 8 -- 279 7 -- 280 8 -- 281 9 -- 283 4 -- 286 7 -- 431 6 -- 448 5 -- 465 8
-- 519 7 -- 539 10 -- 540 12 -- 558 11 -- 569 12 -- 582 13 -- 612 9 -- 622 8 -- 631 6 -- 647 9
-- 647 8 -- 665 7 -- 729 8 -- 731 9 -- 744 10 -- 778 3 -- 800 5 -- 824 6 -- 858 7 -- 875 4 -- 882 5
-- 962 6 -- 993 7 -- 

783 107 7.317757009345795 4.672828834461906

'''
