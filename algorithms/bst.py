class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to do inorder tree traversal

def insert(root, key):
    if root is None:
        return

    if key <= root.val:
        if root.left is None:
            root.left = Node(key)
        else:
            insert(root.left, key)
    if key > root.val:
        if root.right is None:
            root.right = Node(key)
        else:
            insert(root.right, key)


def search(root, key):
    if root is None:
        return False
    if root.val == key:
        return True
    if key < root.val:
        return search(root.left, key)
    else:
        return search(root.right, key)

def dfs(root):
    if root is None:
        return
    dfs(root.left)
    print(root.val)
    dfs(root.right)


class BSTOperation:
    last_value = -1

    def is_bst(self, root):
        if root is None:
            return
        self.is_bst(root.left)
        if root.val < self.last_value:
            return False
        last_value = root.val
        self.is_bst(root.right)
        return True

# Driver program to test the above functions
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80

r = Node(50)
insert(r, 30, )
insert(r, 20)
insert(r, 40, )
insert(r, 70, )
insert(r, 60, )
insert(r, 80, )

# Print inoder traversal of the BST
# inorder(r)
