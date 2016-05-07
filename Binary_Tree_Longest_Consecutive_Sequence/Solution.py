__author__ = 'fengpeng'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestConsecutive(self, root):
        if not root:
                return 0
        return max(self.dfs(root.left, 1, root.val), self.dfs(root.right, 1, root.val))

    def dfs(self, root, count, val):
        if not root:
            return count
        if val - root.val == 1:
            count += 1
        else:
            count = 1
        left = self.dfs(root.left, count, root.val)
        right = self.dfs(root.right, count, root.val)
        return max(left, right, count)


    # solution 2
    def longestConsecutive(self, root):
        if not root:
            return 0
        max = [0]
        self.dfs(None, root, 1, max)
        return max[0]

    def dfs(self, parent, root, count, m):
        if not root:
            return
        if not parent or parent.val - root.val != 1:
            count = 1
        else:
            count += 1
        m[0] = max(m[0], count)
        self.dfs(root, root.left, count, m)
        self.dfs(root, root.right, count, m)


root = TreeNode(6)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.left.right = TreeNode(2)

print Solution().longestConsecutive(root)