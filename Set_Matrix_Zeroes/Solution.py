__author__ = 'fengpeng'


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])

        rows, cols = [False] * m, [False] * n
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    rows[i], cols[j] = True, True

        for i in xrange(m):
            for j in xrange(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0

    # constant space
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])

        fr, fc = False, False
        for i in xrange(m):
            if matrix[i][0] == 0:
                fc = True
                break
        for i in xrange(n):
            if matrix[0][i] == 0:
                fr = True
                break
        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if fr:
            for i in xrange(n):
                matrix[0][i] = 0
        if fc:
            for i in xrange(m):
                matrix[i][0] = 0