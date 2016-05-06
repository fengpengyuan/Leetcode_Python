__author__ = 'fengpeng'


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        while num % 5 == 0:
            num /= 5
        while num % 3 == 0:
            num /= 3
        while num % 2 == 0:
            num /= 2
        return num == 1

    def isUgly(self, num):
        if num==0:
            return False
        if num==1:
            return True
        if num%2==0:
            return self.isUgly(num/2)
        if num%3==0:
            return self.isUgly(num/3)
        if num%5==0:
            return self.isUgly(num/5)
        return False


print Solution().isUgly(12)