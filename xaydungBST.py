class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert_bst(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
    return root


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.key] + inorder(root.right)


# Dữ liệu
arr = [50, 30, 70, 20, 40, 60, 80]
bst_root = None
for x in arr:
    bst_root = insert_bst(bst_root, x)

print("BST (in-order):", inorder(bst_root))
