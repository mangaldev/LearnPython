class Solution:
    result = 0

    def find_average_nodes(self, root):
        self.dfs(root)

    def dfs(self, root):
        #  terminating condition
        if root is None:
            return
        # pre-process

        (lsum, lcount) = self.dfs(root.left)
        (rsum, rcount) = self.dfs(root.right)

        # post- process
        if root.val == (lsum + rsum + root.val) // (lcount + rcount + 1):
            self.result += 1

        return (lsum + rsum + root.val, lcount + rcount + 1)
