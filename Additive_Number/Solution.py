__author__ = 'fengpeng'


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in xrange(1, len(num) - 1):
            for j in xrange(i + 1, len(num)):
                if self.dfs(num, 0, i, j):
                    return True
        return False

    def dfs(self, num, start, end1, end2):
        str1 = num[start: end1]
        str2 = num[end1: end2]

        if (len(str1) > 1 and str1[0] == '0') or (len(str2) > 1 and str2[0] == '0'):
            return False
        # print str1, str2
        num1, num2 = long(str1), long(str2)
        sum = str(num1 + num2)
        if end2 == len(num):
            return True
        if num[end2:].find(sum) != 0:
            return False
        return self.dfs(num, end1, end2, end2 + len(sum))


    def isAdditiveNumber2(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        for i in xrange(1, len(num) - 1):
            if i > 1 and num[0] == '0':
                break
            for j in xrange(i + 1, len(num)):
                first, second, third = 0, i, j
                if num[second] == '0' and third > second + 1:
                    break
                while third < len(num):
                    s1, s2 = num[first:second], num[second:third]
                    sum = str(long(s1) + long(s2))
                    if num[third:].startswith(sum):
                        first, second, third = second, third, third + len(sum)
                    else:
                        break
                if third == len(num):
                    return True
        return False


print Solution().isAdditiveNumber("111")
print Solution().isAdditiveNumber2("011235")

