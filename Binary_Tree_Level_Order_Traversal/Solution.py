__author__ = 'fengpeng'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        que = [root]
        level = []
        curlevel, nextlevel = 1, 0
        while que:
            node = que.pop(0)
            level.append(node.val)
            curlevel -= 1
            if node.left:
                que.append(node.left)
                nextlevel += 1
            if node.right:
                que.append(node.right)
                nextlevel += 1
            if curlevel == 0:
                res.append(level)
                level = []
                curlevel = nextlevel
                nextlevel = 0
        return res