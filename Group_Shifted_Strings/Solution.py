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

    def groupStrings2(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for s in strings:
            mask = tuple([(ord(c) - ord(s[0])) % 26 for c in s])
            d[mask].append(s)
        return map(sorted, d.values())


strings = ["xyz", "abc", "bcd", "acef", "az", "ba", "a", "z"]

print Solution().groupStrings(strings)
print Solution().groupStrings2(strings)
