__author__ = 'fengpeng'


class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        t, base = x, 1
        while t >= 10:
            t /= 10
            base *= 10
        while x > 0:
            last = x % 10
            first = x / base
            if last != first:
                return False
            x %= base
            x /= 10
            base /= 100
        return True

    def isPalindrome2(self, x):
        if x < 0 or x != 0 and x % 10 == 0:
            return False
        res = 0
        t = x
        while x > 0:
            res = res * 10 + x % 10
            x /= 10
        return res == t


Solution().isPalindrome2(1)
