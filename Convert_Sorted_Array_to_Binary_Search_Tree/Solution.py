__author__ = 'fengpeng'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, start, end):
        if start > end:
            return None
        m = (start + end) / 2
        root = TreeNode(nums[m])
        root.left = self.helper(nums, start, m - 1)
        root.right = self.helper(nums, m + 1, end)
        return root

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print root.val,
        self.inorder(root.right)


nums = [1, 2, 3, 4, 5, 6]

root = Solution().sortedArrayToBST(nums)

Solution().inorder(root)