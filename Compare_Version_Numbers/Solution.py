__author__ = 'fengpeng'


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        vs1 = version1.split('.')
        vs2 = version2.split('.')
        if len(vs1) > len(vs2):
            vs2 += ['0'] * (len(vs1) - len(vs2))
        if len(vs2) > len(vs1):
            vs1 += ['0'] * (len(vs2) - len(vs1))
        i = 0
        while i < len(vs1) and i < len(vs2):
            if int(vs1[i]) < int(vs2[i]):
                return -1
            elif int(vs1[i]) > int(vs2[i]):
                return 1
            i += 1
        return 0


    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        vs1 = version1.split('.')
        vs2 = version2.split('.')
        l = max(len(vs1), len(vs2))
        for i in xrange(l):
            num1 = 0
            if i<len(vs1):
                num1 = int(vs1[i])
            num2 = 0
            if i<len(vs2):
                num2 = int(vs2[i])
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        return 0

print Solution().compareVersion("1", "1.0")