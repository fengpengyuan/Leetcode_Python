__author__ = 'fengpeng'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        res = []
        stk = []
        cur = root
        while cur is not None:
            stk.append(cur)
            cur = cur.left
        while stk:
            top = stk.pop()
            res.append(top.val)
            if top.right is not None:
                top = top.right
                while top is not None:
                    stk.append(top)
                    top = top.left
        return res


s = [1, 2, 3, 0]
print(s)
s.reverse()
print(s)

