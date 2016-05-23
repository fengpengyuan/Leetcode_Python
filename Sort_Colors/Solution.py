__author__ = 'fengpeng'


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        i, j, k = 0, len(nums) - 1, len(nums) - 1
        while i <= j:
            if nums[i] == 0:
                i += 1
            elif nums[i] == 1:
                nums[i] = nums[j]
                nums[j] = 1
                j -= 1
            else:
                nums[i] = nums[k]
                nums[k] = 2
                k -= 1
                if j > k:
                    j = k

nums = [0,2,1,0,2,1,1,0]

Solution().sortColors(nums)
print nums