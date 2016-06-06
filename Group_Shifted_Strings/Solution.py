import collections

__author__ = 'fengpeng'


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dict = collections.defaultdict(list)
        for string in strings:
            s = self.getMask(string)
            dict[s].append(string)
        return [sorted(v) for v in dict.values()]

    def getMask(self, st):
        mask = ''
        for i in xrange(1, len(st)):
            mask += str((ord(st[i]) - ord(st[i - 1]) + 26) % 26)
        return mask


strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

print Solution().groupStrings(strings)
