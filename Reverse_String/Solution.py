__author__ = 'fengpeng'


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss=list(s)

        ss.reverse()

        return "".join(ss)

    def reverseString2(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join(reversed(list(s)))



print Solution().reverseString2("hello")