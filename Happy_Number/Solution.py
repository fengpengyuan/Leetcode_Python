__author__ = 'fengpeng'


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set([n])
        while n != 1:
            s = 0
            while n > 0:
                s += pow(n % 10, 2)
                n/=10
            if s in visited:
                return False
            visited.add(s)
            n = s
        return True

print Solution().isHappy(12)