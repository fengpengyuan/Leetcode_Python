__author__ = 'fengpeng'


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1 or num > 3999:
            return ""
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X",
                 "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ""
        for i in xrange(len(roman)):
            while num >= values[i]:
                res += roman[i]
                num -= values[i]
        return res