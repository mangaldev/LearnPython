import collections


class Tree:
    class TreeNode:
        def __init__(self, left, right, value):
            self.left = left
            self.right = right
            self.val = value

    def add_node(self, val):
        return self.TreeNode(None, None, val)

    def breadth_first(self, root):
        if not root:
            return

        queue = collections.deque()
        queue.append(root)
        index = 0
        while index < len(queue):
            node = queue.popleft()
            # do something with this node, save it
            if (node):
                print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


t = Tree()
root = t.add_node(3)
left_root = t.add_node(1)
right_root = t.add_node(2)
root.left = left_root
root.right = right_root

left_left_root = t.add_node(4)
left_root.left = left_left_root

left_right_root = t.add_node(5)
left_root.right = left_right_root

t.breadth_first(root)
