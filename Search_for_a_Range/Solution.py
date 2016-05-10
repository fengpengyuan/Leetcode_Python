__author__ = 'fengpeng'


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j, idx = 0, len(nums) - 1, -1
        while i <= j:
            mid = (i + j) / 2
            if nums[mid] == target:
                idx = mid
                break
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        if idx == -1:
            return [-1, -1]
        res = []
        beg, end = 0, idx
        while beg <= end:
            m = (beg + end) / 2
            if nums[m] < target:
                beg = m + 1
            else:
                end = m - 1

        res.append(beg)

        beg, end = idx, len(nums) - 1
        while beg <= end:
            m = (beg + end) / 2
            if nums[m] > target:
                end = m - 1
            else:
                beg = m + 1
        res.append(end)
        return res

    def searchRange2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        i, j = 0, len(nums)-1
        while i < j:
            m = (i + j) / 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m
        if nums[i] != target:
            return res
        res[0] = i
        j = len(nums)-1

        while i <= j:
            m = (i + j) / 2
            print i, j, m
            if nums[m] > target:
                j = m - 1
            else:
                i = m + 1
        res[1] = j
        return res


nums = [1]

print Solution().searchRange2(nums, 1)
