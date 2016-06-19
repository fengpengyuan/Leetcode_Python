__author__ = 'fengpeng'


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(n, k, [], res, 1)
        return res

    def helper(self, n, k, sol, res, cur):
        if len(sol) == k:
            res.append(list(sol))
        for i in xrange(cur, n+1):
            self.helper(n, k, sol+[i], res, i + 1)

print Solution().combine(4, 2)