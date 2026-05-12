class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return  0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def right_rotate(y):
    print("Rotate right on node", y.data)
    x = y.left
    t2 = x.right
    x.right = y
    y.left = t2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def left_rotate(x):
    print('Rotate left on node',x.data)
    y = x.right
    t2 = y.left
    y.left = x
    x.right = t2
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def insert(node, data):
    if not node:
        return TreeNode(data)

    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)

    # update the balance factor and balance tree and the height of each node based
    # on the position. the height is counted based on the node, not edges.

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)

    # Balancing the tree
    # left left
    if balance > 1 and get_balance(node.left) >= 0:
         return right_rotate(node)

    #left right
    if balance > 1 and get_balance(node.left) < 0:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # right right
    if balance < -1 and get_balance(node.right) <= 0:
        return left_rotate(node)

    # right left

    if balance < -1 and get_balance(node.left) > 0:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node


def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node, data):
    if not node:
        return node

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        temp = min_value_node(node.right)
        node.data = temp.data
        node.right = delete(node.right, temp.data)

    if node is None:
        return node

    # Update the balance factor and balance the tree
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)

    # Balancing the tree
    # Left Left
    if balance > 1 and get_balance(node.left) >= 0:
        return right_rotate(node)

    # Left Right
    if balance > 1 and get_balance(node.left) < 0:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # Right Right
    if balance < -1 and get_balance(node.right) <= 0:
        return left_rotate(node)

    # Right Left
    if balance < -1 and get_balance(node.right) > 0:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node
def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data, end=", ")
    in_order_traversal(node.right)


root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
    root = insert(root, letter)

in_order_traversal(root)
print('\nDeleting A')
root = delete(root,'A')
in_order_traversal(root)
