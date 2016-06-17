import collections

__author__ = 'fengpeng'


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        dict = {}
        for i in xrange(len(s) - 9):
            seq = s[i:i + 10]
            mask = self.encode(seq)
            if mask in dict and dict[mask] == 1:
                res.append(seq)
                dict[mask] = 2
            elif mask not in dict:
                dict[mask] = 1
        return res

    def encode(self, s):
        code = 0
        for c in s:
            code <<= 2
            if c == 'A':
                code += 0
            elif c == 'C':
                code += 1
            elif c == 'T':
                code += 2
            else:
                code += 3
        return code


print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")


