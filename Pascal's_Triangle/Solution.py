__author__ = 'fengpeng'


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        res = [[1 for j in xrange(i)] for i in xrange(1, numRows+1)]
        for i in xrange(1, numRows):
            for j in xrange(1, i + 1):
                if j == 0 or j == i:
                    res[i][j] = 1
                else:
                    res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res

    def generate2(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res, pre = [], []
        for i in xrange(numRows):
            row = []
            for j in xrange(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(pre[j] + pre[j - 1])
            res.append(row)
            pre = row

        return res

    def generate3(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows<1:
            return []
        res=[[1]]

        for i in xrange(1, numRows):
            row=[1]
            for j in xrange(1, i):
                row.append(res[i-1][j]+res[i-1][j-1])
            row.append(1)
            res.append(row)
        return res


print Solution().generate3(5)
print Solution().generate2(5)

