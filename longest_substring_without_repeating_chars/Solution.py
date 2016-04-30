__author__ = 'fengpeng'


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxLength = start = 0
        dic = {}
        for i in range(len(s)):
            if s[i] in dic and start <= dic.get(s[i]):
                start = dic.get(s[i]) + 1
            else:
                maxLength = max(maxLength, i-start+1)
            dic[s[i]] = i
        return maxLength


print(Solution().lengthOfLongestSubstring("tmmzuxt"))