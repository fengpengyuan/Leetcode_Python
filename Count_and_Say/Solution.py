__author__ = 'fengpeng'


class Solution(object):
    # def countAndSay(self, n):
    # """
    #     :type n: int
    #     :rtype: str
    #     """
    #     s=str(n)
    #     count =1
    #     res=""
    #     for i in xrange(1, len(s)):
    #         if s[i]==s[i-1]:
    #             count+=1
    #         else:
    #             res+=str(count)+s[i-1]
    #             count=1
    #
    #     res+=str(count)+s[-1]
    #     return res


    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return ""
        s = "1"
        for i in xrange(n - 1):
            count = 1
            temp = ""
            for j in xrange(1, len(s)):
                if s[j] == s[j - 1]:
                    count += 1
                else:
                    temp += str(count) + s[j - 1]
                    count = 1
            temp += str(count) + s[-1]
            s = temp
        return s


print Solution().countAndSay(2)