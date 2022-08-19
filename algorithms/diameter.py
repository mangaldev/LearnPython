# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.dia(root)
        return self.result - 1

    result = 0

    def dia(self, root):
        if root is None:
            return 0

        leftH = self.dia(root.left)
        rightH = self.dia(root.right)

        self.result = max(self.result, leftH + rightH + 1)

        return max(leftH, rightH) + 1
