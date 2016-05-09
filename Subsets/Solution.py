__author__ = 'fengpeng'


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, [], res, 0)
        return res

    def dfs(self, nums, sol, res, cur):
        res.append([] + sol)

        for i in xrange(cur, len(nums)):
            sol.append(nums[i])
            self.dfs(nums, sol, res, i + 1)
            sol.pop()


nums = [1, 2, 3]

print Solution().subsets(nums)
