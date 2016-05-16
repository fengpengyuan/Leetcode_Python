__author__ = 'fengpeng'


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, que = [], []
        que.append((root, 0))
        dict = {}
        while que:
            node, col = que.pop(0)
            if col in dict:
                dict[col].append(node.val)
            else:
                dict[col] = [node.val]
            if node.left:
                que.append((node.left, col - 1))
            if node.right:
                que.append((node.right, col + 1))

        keys = sorted(dict.keys())
        for key in keys:
            res.append(dict.get(key))
        return res


root = TreeNode(5)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right = TreeNode(8)
root.right.right = TreeNode(11)
root.right.left = TreeNode(7)

print Solution().verticalOrder(root)