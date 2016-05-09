__author__ = 'fengpeng'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

    def helper(self, preorder, beg1, end1, inorder, beg2, end2):
        if beg1 > end1:
            return None
        root = TreeNode(preorder[beg1])
        index = inorder.index(root.val)
        l = index - beg2
        root.left = self.helper(preorder, beg1 + 1, beg1 + l, inorder, beg2, index - 1)
        root.right = self.helper(preorder, beg1 + l + 1, end1, inorder, index + 1, end2)
        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root = TreeNode(preorder.pop(0))
            index = inorder.index(root.val)
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root



inorder = [1,2]
preorder = [1,2]

print Solution().buildTree(preorder, inorder).val