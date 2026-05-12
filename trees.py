"""
Arrays, Linked Lists, Stacks, and Queues.
These are all linear structures, which means that each element follows directly after another
in a sequence. Trees however, are different. In a Tree, a single element can have multiple
next' elements, allowing the data structure to branch out in various directions.
"""
from fontTools.misc.cython import returns


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# preorder traversal
def pre_order_traversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)


# inorder traversal
def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.data, end=", ")
    inorder_traversal(node.right)


# Post-order traversal
def post_order_traversal(node):
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data, end=", ")


root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')


root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print("root.right.right.left.data:", root.right.right.left.data)

print()
print("pre order traversal:")
pre_order_traversal(root)


print()
print()
print("inorder traversal:")
inorder_traversal(root)

print()
print()
print("post order traversal:")
post_order_traversal(root)
print()


#Binary Search Tree BST

rootbst = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)


def search(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)


def insert(node, data):
    if node is None:
        return  TreeNode(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current



def delete(node, data):
    if not node:
        return None
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.righ, data)
    else:
        #Node with one or not child
        if not node.right:
            temp = node.left
            node = None
            return temp
        elif not node.left:
            temp = node.left
            temp = node.right
            node = None
            return temp

        # Node with two children:
        # we call the min_value_node on node.right to get the in-order successor
        node.data = min_value_node(node.right).data
        node.right = delete(node.right, node.data)

    return node

rootbst.left = node7
rootbst.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

print()
print("in order traversal of BST")
inorder_traversal(rootbst)
print()
print("we want to search for number 14",search(rootbst, 14).data)
print()
print("we want to insrt the number 24" )
insert(rootbst, 24)
print()
inorder_traversal(rootbst)



# AVL tree













































