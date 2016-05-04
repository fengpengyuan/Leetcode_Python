__author__ = 'fengpeng'


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        vowels = 'aeiouAEIOU'
        ss = list(s)
        i, j = 0, len(ss) - 1

        while i < j:
            while i < j and ss[i] not in vowels:
                i += 1
            while i < j and ss[j] not in vowels:
                j -= 1
            if i < j:
                c = ss[i]
                ss[i] = ss[j]
                ss[j] = c
                i += 1
                j -= 1
        return "".join(ss)


print Solution().reverseVowels("abcdA")