import sys

__author__ = 'fengpeng'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root or k <= 0:
            return -sys.maxint - 1
        lcount = self.countNodes(root.left)
        if lcount == k - 1:
            return root.val
        elif lcount < k - 1:
            return self.kthSmallest(root.right, k - lcount - 1)
        else:
            return self.kthSmallest(root.left, k)

    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def kthSmallest(self, root, k):
        if not root or k <= 0:
            return sys.maxint
        stk, count, cur = [], 0, root
        while cur:
            stk.append(cur)
            cur = cur.left
        while stk:
            top = stk.pop()
            count += 1
            if count == k:
                return top.val
            if top.right:
                top = top.right
                while top:
                    stk.append(top)
                    top = top.left
        return sys.maxint


root = TreeNode(5)
root.left = TreeNode(2)
root.left.left = TreeNode(1)

root.left.right = TreeNode(3)

root.right = TreeNode(8)
root.right.left = TreeNode(6)

print -sys.maxint - 1

print Solution().kthSmallest(root, 3)