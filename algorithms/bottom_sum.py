class Solution:
    sum = 0

    max_height = 0

    def find_bottom_sum(self, root):
        self.dfs(root, 0)

    def dfs(self, root, height):
        #  terminating condition
        if root is None:
            return
        #  pre-process

        if height == self.max_height:
            self.sum += root.val

        if height > self.max_height:
            self.max_height = height
            self.sum = root.val

        self.dfs(root.left, height + 1)
        self.dfs(root.right, height + 1)



