class Solution(object):
    index = 0
    visted_counter = 0
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.index = k
        self.smallest(root)
        return self.result

    def smallest(self, root):
        if root is None:
            return

        if self.index < 0:
            return

        self.smallest(root.left)
        self.index -= 1

        if self.index == 0:
            self.result = root.val
            return

        self.smallest(root.right)

    def smallest_1(self, root, k):
        if root is None:
            return

        self.smallest_1(root.left, k)

        self.visted_counter += 1
        if k == self.visted_counter:
            print("reached the required node")
            self.result = root.val

        self.smallest_1(root.right, k)