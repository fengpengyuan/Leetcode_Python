__author__ = 'fengpeng'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None]
        res = []
        for i in xrange(start, end + 1):
            leftNodes = self.helper(start, i - 1)
            rightNodes = self.helper(i + 1, end)

            for left in leftNodes:
                for right in rightNodes:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res
