__author__ = 'fengpeng'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        res, path = [], []
        self.pathSumUtil(root, sum, 0, path, res)
        return res

    def pathSumUtil(self, root, sum, curSum, path, res):
        if not root:
            return
        curSum += root.val
        path.append(root.val)
        if root.left is None and root.right is None and curSum == sum:
            cur = list(path)# create a new list, in python vairables are tags of the attached to objects
            res.append(cur)
        self.pathSumUtil(root.left, sum, curSum, path, res)
        self.pathSumUtil(root.right, sum, curSum, path, res)
        curSum -= root.val
        path.pop()


