__author__ = 'fengpeng'


class Solution(object):
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + carry
            carry = s / 10
        return [1] + digits if carry == 1 else digits


digits = [1, 2, 5]
# Solution().plusOne(digits)

print(digits.append(3))