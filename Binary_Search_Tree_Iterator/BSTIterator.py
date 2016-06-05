__author__ = 'fengpeng'


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stk = []
        while root:
            self.stk.append(root)
            root = root.left


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stk


    def next(self):
        """
        :rtype: int
        """
        res = self.stk.pop()
        if res.right:
            right = res.right
            while right:
                self.stk.append(right)
                right = right.left
        return res.val



        # Your BSTIterator will be called like this:
        # i, v = BSTIterator(root), []
        # while i.hasNext(): v.append(i.next())
root= TreeNode(1)
root.left=TreeNode(2)
root.left.right = TreeNode(3)
root.right=TreeNode(4)
root.right.right=TreeNode(5)

i, v = BSTIterator(root), []

while i.hasNext():
    v.append(i.next())
print v