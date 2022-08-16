class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


node = TreeNode(5)
node.left = TreeNode(3)
node.right = TreeNode(7)



class Tree:
    sum = 0
    def preorder(self, root):
        if root is None:
            return
        self.operation(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.operation(root.val)
        self.inorder(root.right)

    def operation(self,val):
        self.sum = self.sum + val

tree = Tree()

tree.preorder(node)

print(tree.sum)



