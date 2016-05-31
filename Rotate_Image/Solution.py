__author__ = 'fengpeng'


class Solution(object):
    # Rotate the image by 90 degrees (clockwise).
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            for j in xrange(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

                # for i in xrange(m):
                # left, right = 0, n - 1
                #     while left < right:
                #         matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                #         left += 1
                #         right -= 1

    # Rotate the image by 90 degrees (anti-clockwise).
    def rotate2(self, matrix):
        for row in matrix:
            row.reverse()
        for i in xrange(len(matrix)):
            for j in xrange(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print matrix
Solution().rotate2(matrix)
print matrix
