__author__ = 'fengpeng'


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row, pre = [], []

        for i in xrange(rowIndex + 1):
            row = []
            for j in xrange(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(pre[j] + pre[j - 1])
            pre = row
        return row


print Solution().getRow(3)