__author__ = 'fengpeng'


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        cur, parent, right = root, None, None
        while cur:
            left = cur.left
            cur.left = right
            right = cur.right
            cur.right = parent
            parent = cur
            cur = left
        return parent

    def upsideDownBinaryTree2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or (not root.left and not root.right):
            return root
        res = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root

        root.left = root.right = None
        return res

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print root.val,
        self.inorder(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left=TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)

Solution().inorder(root)
print
r = Solution().upsideDownBinaryTree2(root)
Solution().inorder(r)


