__author__ = 'fengpeng'


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, sol = [], []
        used = [False] * len(nums)
        self.permuteUtil(nums, res, sol, used)
        return res

    def permuteUtil(self, nums, res, sol, used):
        if len(sol) == len(nums):
            res.append(sol + [])
            return
        for i in xrange(len(nums)):
            if not used[i]:
                sol.append(nums[i])
                used[i] = True
                self.permuteUtil(nums, res, sol, used)
                sol.pop()
                used[i] = False

    # iterative
    def permute2(self, nums):
        res = [[]]
        for i in xrange(len(nums)):
            curr = []
            for sol in res:
                # for j in xrange(i+1):
                for j in xrange(len(sol)+1):
                    newSol = sol[:j] + [nums[i]] + sol[j:]
                    curr.append(newSol)
            res = curr
        return res


nums = [1, 2, 3]

print Solution().permute(nums)
print Solution().permute2(nums)