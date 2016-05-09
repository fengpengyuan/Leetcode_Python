__author__ = 'fengpeng'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def helper(self, inorder, beg1, end1, postorder, beg2, end2):
        if beg1 > end1:
            return None
        root = TreeNode(postorder[end2])
        index = inorder.index(root.val)

        l = index - beg1
        root.left = self.helper(inorder, beg1, index - 1, postorder, beg2, beg2 + l - 1)
        root.right = self.helper(inorder, index + 1, end1, postorder, beg2 + l, end2 - 1)

        return root

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            print inorder, postorder
            root = TreeNode(postorder.pop())
            index = inorder.index(root.val)
            root.right = self.buildTree(inorder[index + 1:], postorder)
            root.left = self.buildTree(inorder[:index], postorder)
            return root


inorder = [2, 1, 3]
postorder = [2, 3, 1]

print Solution().buildTree(inorder, postorder).val