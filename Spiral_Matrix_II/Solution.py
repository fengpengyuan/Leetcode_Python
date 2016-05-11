__author__ = 'fengpeng'


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in xrange(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        num = 1
        while True:
            for i in xrange(left, right + 1):
                res[top][i] = num
                num += 1
            top += 1
            if top > bottom:
                break
            for j in xrange(top, bottom + 1):
                res[j][right] = num
                num += 1
            right -= 1
            if right < left:
                break
            for i in xrange(right, left - 1, -1):
                res[bottom][i] = num
                num += 1
            bottom -= 1
            if bottom < top:
                break
            for j in xrange(bottom, top - 1, -1):
                res[j][left] = num
                num += 1
            left += 1
            if left > right:
                break
        return res

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in xrange(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        num = 1

        while left < right and top < bottom:
            for i in xrange(left, right):
                res[top][i] = num
                num += 1
            for i in xrange(top, bottom):
                res[i][right] = num
                num += 1
            for i in xrange(right, left, -1):
                res[bottom][i] = num
                num += 1
            for i in xrange(bottom, top, -1):
                res[i][left] = num
                num += 1
            left, right, bottom, top = left + 1, right - 1, bottom - 1, top + 1

        if left == right:
            res[left][right] = num
        return res


print Solution().generateMatrix(4)