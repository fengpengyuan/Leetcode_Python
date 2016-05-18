__author__ = 'fengpeng'


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        if not nums:
            res.append(self.getRange(lower, upper))
            return res

        if nums[0] > lower:
            res.append(self.getRange(lower, nums[0] - 1))
        for i in xrange(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                res.append(self.getRange(nums[i - 1]+1, nums[i]-1))
        if upper > nums[-1]:
            res.append(self.getRange(nums[-1] + 1, upper))
        return res

    def getRange(self, lower, upper):
        if lower == upper:
            return str(lower)
        else:
            return str(lower)+"->"+str(upper)


nums=[2, 3, 17, 50, 75, 99]
print Solution().findMissingRanges(nums, 0, 99)