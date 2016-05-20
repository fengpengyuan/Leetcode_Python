__author__ = 'fengpeng'


class SegmentTreeNode(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
        self.sum = 0


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.root = self.buildTree(nums, 0, len(nums) - 1)

    def buildTree(self, nums, start, end):
        if start > end:
            return None
        res = SegmentTreeNode(start, end)
        if start == end:
            res.sum = nums[start]
        else:
            m = (start + end) / 2
            res.left = self.buildTree(nums, start, m)
            res.right = self.buildTree(nums, m + 1, end)
            res.sum = res.left.sum + res.right.sum
        return res

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.updateHelper(self.root, i, val)

    def updateHelper(self, root, i, val):
        if root.start == root.end:
            root.sum = val
        else:
            m = (root.start + root.end) / 2
            if i <= m:
                self.updateHelper(root.left, i, val)
            else:
                self.updateHelper(root.right, i, val)
            root.sum = root.left.sum + root.right.sum


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumRangeHelper(self.root, i, j)

    def sumRangeHelper(self, root, i, j):
        if root.start == i and root.end == j:
            return root.sum
        m = (root.start + root.end) / 2
        if j <= m:
            return self.sumRangeHelper(root.left, i, j)
        if i > m:
            return self.sumRangeHelper(root.right, i, j)
        else:
            return self.sumRangeHelper(root.left, i, m) + self.sumRangeHelper(root.right, m + 1, j)


# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 4]
numArray = NumArray(nums)
print numArray.sumRange(0, 1)
print numArray.update(1, 0)
print numArray.sumRange(1, 2)