__author__ = 'fengpeng'


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        step = 1
        max, min = nums[0], 0
        while max < n - 1:
            t = max
            for i in xrange(min, t + 1):
                if i + nums[i] > max:
                    max = i + nums[i]
                    min = i
            step += 1
        return step

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        step = [-1] * n
        step[0] = 0

        for i in xrange(1, n):
            for j in xrange(i):
                if step[j] != -1 and j + step[j] >= i:
                    step[i] = step[j] + 1
        return step[n - 1]


    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_jump_max, cur_jump_max, step = 0, 0, 0

        for i in xrange(len(nums) - 1):
            cur_jump_max = max(cur_jump_max, i + nums[i])
            if i == last_jump_max:
                step += 1
                last_jump_max = cur_jump_max
        return step

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end, step = 0, 0, 0
        while end < len(nums) - 1:
            farthest = end
            for i in xrange(start, end + 1):
                farthest = max(farthest, i + nums[i])
            step += 1
            start = end + 1
            end = farthest
        return step


A = [1, 2, 3]

print Solution().jump(A)