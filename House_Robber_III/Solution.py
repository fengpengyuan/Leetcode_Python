__author__ = 'fengpeng'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left = self.rob(root.left)
        right = self.rob(root.right)
        ll, lr, rl, rr = 0, 0, 0, 0
        if root.left:
            ll = self.rob(root.left.left)
            lr = self.rob(root.left.right)
        if root.right:
            rl = self.rob(root.right.left)
            rr = self.rob(root.right.right)
        return max(left + right, ll + lr + root.val + rl + rr)

    def rob2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        map = {}
        return self.helper(root, map)

    def helper(self, root, map):
        if not root:
            return 0
        if root in map:
            return map[root]

        left = self.helper(root.left, map)
        right = self.helper(root.right, map)
        ll, lr, rl, rr = 0, 0, 0, 0
        if root.left:
            ll = self.helper(root.left.left, map)
            lr = self.helper(root.left.right, map)
        if root.right:
            rl = self.helper(root.right.left, map)
            rr = self.helper(root.right.right, map)
        map[root] = max(left + right, ll + lr + root.val + rl + rr)
        return map[root]

    def rob3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.helper(root))

    def helper(self, root):
        if not root:
            return [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        res = list()
        res.append(max(left) + max(right))
        res.append(root.val + left[0] + right[0])
        return res


root = TreeNode(3)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.right = TreeNode(3)
root.right.right = TreeNode(1)

root1 = TreeNode(3)
root1.left = TreeNode(4)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
root1.right = TreeNode(5)
root1.right.right = TreeNode(1)

print Solution().rob(root)
print Solution().rob2(root1)
