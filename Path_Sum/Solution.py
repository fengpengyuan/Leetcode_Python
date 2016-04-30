__author__ = 'fengpeng'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return False
        return self.pathSumUtil(root, 0, sum)

    def pathSumUtil(self, root, curSum, sum):
        if not root:
            return False
        curSum += root.val
        if root.left is None and root.right is None and curSum == sum:
            return True
        return self.pathSum(root.left, curSum, sum) or self.pathSum(root.right, curSum, sum)
