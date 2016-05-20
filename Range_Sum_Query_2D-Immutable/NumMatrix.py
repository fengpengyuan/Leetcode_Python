__author__ = 'fengpeng'


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        self.matrix = matrix
        m, n = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (n + 1) for _ in xrange(m + 1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                self.sumMat[i][j] = self.sumMat[i][j-1]+self.sumMat[i-1][j]-self.sumMat[i-1][j-1]+matrix[i-1][j-1]

        print self.sumMat


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sumMat[row2+1][col2+1]-self.sumMat[row1][col2+1]-self.sumMat[row2+1][col1]+self.sumMat[row1][col1]



        # Your NumMatrix object will be instantiated and called as such:
mat = [[3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]]

numMatrix = NumMatrix(mat)
print numMatrix.sumRegion(2, 1, 4, 3)
print numMatrix.sumRegion(1, 1, 2, 2)
print numMatrix.sumRegion(1, 2, 2, 4)



