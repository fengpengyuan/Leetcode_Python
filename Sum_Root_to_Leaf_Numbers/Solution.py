__author__ = 'fengpeng'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumNumbersUtil(root, 0)

    def sumNumbersUtil(self, root, sum):
        if not root:
            return 0
        sum = sum * 10 + root.val
        if not root.left and not root.right:
            return sum
        return self.sumNumbersUtil(root.left, sum) + self.sumNumbersUtil(root.right, sum)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print Solution().sumNumbers(root)