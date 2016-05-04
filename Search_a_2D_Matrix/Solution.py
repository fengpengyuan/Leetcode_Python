__author__ = 'fengpeng'


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        i, j = 0, m * n - 1

        while i <= j:
            mid = (j - i) / 2 + i
            midRow = mid / n
            midCol = mid % n
            if matrix[midRow][midCol] == target:
                return True
            elif matrix[midRow][midCol] > target:
                j -= 1
            else:
                i += 1
        return False
