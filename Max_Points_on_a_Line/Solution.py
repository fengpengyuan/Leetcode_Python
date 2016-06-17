import collections

__author__ = 'fengpeng'


# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 3:
            return len(points)
        res = 1

        for i in xrange(len(points) - 1):
            p1 = points[i]
            dup = 0
            vertical = 1
            curmax = 1
            dict = {}
            for j in xrange(i + 1, len(points)):
                p2 = points[j]
                if p1.x == p2.x:
                    if p1.y == p2.y:
                        dup += 1
                    else:
                        vertical += 1
                else:
                    k = 0 if p1.y == p2.y else 1.0 * (p1.y - p2.y) / (p1.x - p2.x)
                    if k in dict:
                        dict[k] += 1
                    else:
                        dict[k] = 2
                    if dict[k] > curmax:
                        curmax = dict[k]
            print dict
            res = max(res, curmax + dup, vertical + dup)
        return res


points = [Point(0, 0), Point(-1, -1), Point(2, 2)]

print Solution().maxPoints(points)