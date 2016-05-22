__author__ = 'fengpeng'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        que = [root]
        res, level = [], []
        curlevel, nextlevel = 1, 0
        l2r = True
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
                if not l2r:
                    level.reverse()
                res.append(level)
                level = []
                l2r = not l2r
                curlevel = nextlevel
                nextlevel = 0
        return res

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)

Solution().zigzagLevelOrder(root)