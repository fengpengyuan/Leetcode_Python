__author__ = 'fengpeng'


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        if n == 0:
            return []
        m, res = len(matrix[0]), []
        left, right, top, bottom = 0, m - 1, 0, n - 1
        while True:
            for i in xrange(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break

            for i in xrange(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break

            for i in xrange(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if bottom < top:
                break

            for i in xrange(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res

matrix=[[2,3]]
print Solution().spiralOrder(matrix)
