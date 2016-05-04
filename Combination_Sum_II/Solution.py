__author__ = 'fengpeng'


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res, used = [], [False] * len(candidates)

        self.combinationSumUtil(candidates, target, [], res, used, 0)
        return res

    def combinationSumUtil(self, candidates, target, sol, res, used, cur):
        if target < 0:
            return
        if target == 0:
            res.append(list(sol))
            return
        for i in xrange(cur, len(candidates)):
            if i != 0 and candidates[i] == candidates[i - 1] and not used[i - 1]:
                continue
            if not used[i]:
                target -= candidates[i]
                used[i] = True
                sol.append(candidates[i])
                self.combinationSumUtil(candidates, target, sol, res, used, i + 1)
                target += candidates[i]
                used[i] = False
                sol.pop()


nums = [10, 1, 2, 7, 6, 1, 5]

print Solution().combinationSum2(nums, 8)