__author__ = 'fengpeng'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res, stk, cur = [], [root]
        while stk:
            top = stk.pop()
            res.append(top.val)
            if top.right:
                stk.append(top.right)
            if top.left:
                stk.append(top.left)
        return res

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stk = [], [root]
        while stk:
            top = stk.pop()
            if top:
                res.append(top.val)
                stk.append(top.right)
                stk.append(top.left)
        return res