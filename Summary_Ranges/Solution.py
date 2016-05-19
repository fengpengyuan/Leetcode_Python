__author__ = 'fengpeng'


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res, pre = [], nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                res.append(self.getRange(pre, nums[i - 1]))
                pre = nums[i]
        res.append(self.getRange(pre, nums[-1]))
        return res

    def getRange(self, lower, upper):
        if lower == upper:
            return str(lower)
        return str(lower) + "->" + str(upper)


    def summaryRanges2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        start, end, res = 0, 0, []
        while end < len(nums):
            if end + 1 < len(nums) and nums[end + 1] == nums[end] + 1:
                end += 1
            else:
                if start == end:
                    res.append(str(nums[end]))
                else:
                    res.append(str(nums[start]) + "->" + str(nums[end]))
                end += 1
                start = end
        return res


nums = [0, 1, 2, 4, 5, 7]
print Solution().summaryRanges2(nums)