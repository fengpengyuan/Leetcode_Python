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
        i, j = 0, m - 1
        while i <= j:
            mid = (j - i) / 2 + i
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                j -= 1
            else:
                i += 1
        row = j
        if row < 0:
            return False
        i, j = 0, n - 1

        while i <= j:
            mid = (j - i) / 2 + i
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                j -= 1
            else:
                i += 1
        return False