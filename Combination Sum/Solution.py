__author__ = 'fengpeng'


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.combinationSumUtil(candidates, target, [], res, 0)
        return res

    def combinationSumUtil(self, candidates, target, sol, res, cur):
        if target < 0:
            return
        if target == 0:
            res.append(sol + [])
        for i in xrange(cur, len(candidates)):
            target -= candidates[i]
            sol.append(candidates[i])
            self.combinationSumUtil(candidates, target, sol, res, i)
            target += candidates[i]
            sol.pop()


nums=[2, 3, 6, 7]

print Solution().combinationSum(nums, 7)