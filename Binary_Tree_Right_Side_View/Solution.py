__author__ = 'fengpeng'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        que = [root]
        cur, next = 1, 0
        while que:
            node = que.pop(0)
            cur -= 1
            if node.left:
                que.append(node.left)
                next += 1
            if node.right:
                que.append(node.right)
                next += 1
            if cur == 0:
                res.append(node.val)
                cur, next = next, cur

        return res

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, 0, res)
        return res

    def helper(self, root, level, res):
        if not root:
            return
        if len(res) == level:
            res.append(root.val)
        self.helper(root.right, level + 1, res)
        self.helper(root.left, level + 1, res)


    def leftSideView(self, root):
        res = []
        self.leftHelper(root, 0, res)
        return res

    def leftHelper(self, root, level, res):
        if not root:
            return
        if level == len(res):
            res.append(root.val)
        self.leftHelper(root.left, level + 1, res)
        self.leftHelper(root.right, level + 1, res)