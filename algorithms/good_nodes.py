class TreeNode:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.val = value


class Solution:
    result = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.result

    def dfs(self, root, height):
        if root is None:
            return

        if root.val >= height:
            self.result += 1

        self.dfs(root.left, height + 1)
        self.dfs(root.right, height + 1)


a_node = TreeNode(None, None, 2)
b_node = TreeNode(None, None, 1)
c_node = TreeNode(None,None,0)

a_node.left = b_node
a_node.right= c_node

print(Solution().goodNodes(a_node))
