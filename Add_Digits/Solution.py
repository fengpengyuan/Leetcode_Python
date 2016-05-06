__author__ = 'fengpeng'


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
        while num >= 10:
            sum = 0
            while num > 0:
                sum += num % 10
                num /= 10
            num = sum
        return num
        # return 1 + (num-1)%9
