__author__ = 'fengpeng'


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = s.split()

        ss.reverse()
        return ' '.join(ss)


s = "the sky is blue"

print Solution().reverseWords(s)