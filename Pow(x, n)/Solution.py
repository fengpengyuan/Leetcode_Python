__author__ = 'fengpeng'


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        neg = False
        if n<0:
            n=-n
            neg=True
        res = self.myPow(x, n/2)
        if n%2==0:
            res *= res
        else:
            res*= res*x
        if neg:
            return 1/res
        return res

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n<0:
            n=-n
            x=1/x
        if n%2==0:
            return self.myPow(x*x, n/2)
        return self.myPow(x*x, n/2)*x

print Solution().myPow(3.1, 2)