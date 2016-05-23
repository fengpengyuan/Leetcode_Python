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
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
                if j > k:
                    j = k

    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums) - 1
        while i <= k:
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
            else:
                i += 1



nums = [2, 0, 0, 0, 0]

Solution().sortColors(nums)
print nums