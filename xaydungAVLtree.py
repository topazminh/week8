class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def get_height(root):
    return root.height if root else 0


def get_balance(root):
    return get_height(root.left) - get_height(root.right) if root else 0


def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x


def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y


def insert_avl(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert_avl(root.left, key)
    else:
        root.right = insert_avl(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    # Cân bằng
    if balance > 1 and key < root.left.key:      # Left Left
        return rotate_right(root)
    if balance < -1 and key > root.right.key:    # Right Right
        return rotate_left(root)
    if balance > 1 and key > root.left.key:      # Left Right
        root.left = rotate_left(root.left)
        return rotate_right(root)
    if balance < -1 and key < root.right.key:    # Right Left
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.key] + inorder(root.right)


# Dữ liệu
arr = [50, 30, 70, 20, 40, 60, 80]
avl_root = None
for x in arr:
    avl_root = insert_avl(avl_root, x)

print("AVL (in-order):", inorder(avl_root))
