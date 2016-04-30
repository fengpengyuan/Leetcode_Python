__author__ = 'fengpeng'


class Solution(object):
    def isStrobogrammatic(self, num):
        dic = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        beg, end = 0, len(num) - 1

        while beg <= end:
            if num[beg] not in dic or num[end] not in dic or dic.get(num[beg]) != num[end]:
                return False
            beg += 1
            end -= 1
        return True

print(Solution().isStrobogrammatic("101"))

