import sys

__author__ = 'fengpeng'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [-sys.maxint]
        self.helper(root, res)
        return res[0]

    def helper(self, root, res):
        if not root:
            return 0
        lMax = self.helper(root.left, res)
        rMax = self.helper(root.right, res)
        tMax = max(root.val, lMax+root.val, rMax+root.val)
        res[0] = max(res[0], tMax, lMax+root.val+rMax)
        return tMax

    def helper(self, root, res):
        if not root:
            return 0
        lMax = max(0, self.helper(root.left, res))
        rMax = max(0, self.helper(root.right, res))
        res[0] = max(res[0], lMax+root.val+rMax)
        return max(lMax, rMax) + root.val


