__author__ = 'fengpeng'


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums) - 1

        while i <= j:
            mid = (j - i) / 2 + i
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j -= 1
            else:
                i += 1
        return i

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.helper(nums, 0, len(nums)-1, target)

    def helper(self, nums, beg, end, target):
        if beg>end:
            return beg
        mid=(beg+end)/2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            return self.helper(nums, beg, mid-1, target)
        return self.helper(nums, mid+1, end, target)

nums=[1,2,4,7]

print Solution().searchInsert(nums, 3)