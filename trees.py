"""
Arrays, Linked Lists, Stacks, and Queues.
These are all linear structures, which means that each element follows directly after another
in a sequence. Trees however, are different. In a Tree, a single element can have multiple
next' elements, allowing the data structure to branch out in various directions.
"""


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