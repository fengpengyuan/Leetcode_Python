__author__ = 'fengpeng'


class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        for i in xrange(1, n):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        return min(costs[n - 1][0], costs[n - 1][1], costs[n - 1][2])

costs=[[2,1,3],
       [3,1,2],
       [4,2,3],
       [4,5,3]]

print Solution().minCost(costs)