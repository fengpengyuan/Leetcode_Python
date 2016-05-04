__author__ = 'fengpeng'


class Solution(object):
    # def combinationSum3(self, k, n):
    # """
    #     :type k: int
    #     :type n: int
    #     :rtype: List[List[int]]
    #     """
    #     res, sol = [], []
    #     self.combinationSumUtil(k, n, sol, res, 0, 1)
    #     return res
    #
    # def combinationSumUtil(self, k, n, sol, res, curSum, cur):
    #     if curSum > n:
    #         return
    #     if len(sol) == k and curSum == n:
    #         res.append(list(sol))
    #         return
    #     for i in xrange(cur, 10):
    #         curSum += i
    #         sol.append(i)
    #         self.combinationSumUtil(k, n, sol, res, curSum, i+1)
    #         sol.pop()
    #         curSum -= i


    #######################################################################
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res, sol = [], []
        self.combinationSumUtil(k, n, sol, res, 1)
        return res

    def combinationSumUtil(self, k, n, sol, res, cur):
        if n < 0:
            return
        if len(sol) == k and n == 0:
            res.append(list(sol))
            return
        for i in xrange(cur, 10):
            n -= i
            sol.append(i)
            self.combinationSumUtil(k, n, sol, res, i + 1)
            sol.pop()
            n += i


print Solution().combinationSum3(3, 7)