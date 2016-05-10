__author__ = 'fengpeng'


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[i]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return -1


nums = [4, 5, 6, 7, 8, 1, 2, 3]

print Solution().search(nums, 8)