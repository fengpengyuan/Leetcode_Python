__author__ = 'fengpeng'


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1, l2 = len(num1), len(num2)
        res = [0] * (l1 + l2)

        for i in xrange(l1 - 1, -1, -1):
            carry = 0
            for j in xrange(l2 - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                sum = res[i + j + 1] + product + carry
                carry = sum / 10
                sum %= 10
                res[i + j + 1] = sum
            res[i] = carry
        ans = ""
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        if i == len(res):
            return "0"
        while i < len(res):
            ans += str(res[i])
            i += 1
        return ans


print Solution().multiply("112", "2")
