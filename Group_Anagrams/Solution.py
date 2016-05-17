import collections

__author__ = 'fengpeng'


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = collections.defaultdict(list)
        for s in strs:
            t = "".join(sorted(s))
            dict[t].append(s)

        return [sorted(dict[i]) for i in dict]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print Solution().groupAnagrams(strs)

print sorted("abec")