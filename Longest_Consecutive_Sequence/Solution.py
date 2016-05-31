__author__ = 'fengpeng'


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for num in nums:
            s.add(num)
        res = 0
        for num in nums:
            inc = self.helper(num, s, True)
            dec = self.helper(num - 1, s, False)
            res = max(res, inc + dec)
        return res

    def helper(self, num, s, increasing):
        l = 0
        while num in s:
            l += 1
            s.remove(num)
            if increasing:
                num += 1
            else:
                num -= 1
        return l

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for num in nums:
            s.add(num)
        res = 0

        for num in nums:
            count = 0
            t = num
            while t in s:
                count += 1
                s.remove(t)
                t += 1
            t = num - 1
            while t in s:
                count += 1
                s.remove(t)
                t -= 1
            res = max(res, count)
        return res


nums = [100, 4, 200, 1, 3, 2]

print Solution().longestConsecutive(nums)
