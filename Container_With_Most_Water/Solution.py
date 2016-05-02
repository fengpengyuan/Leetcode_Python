__author__ = 'fengpeng'


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        res = 0
        i, j = 0, len(height) - 1

        while i < j:
            h = min(height[i], height[j])
            w = j - i
            res = max(res, h * w)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res
