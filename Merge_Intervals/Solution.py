__author__ = 'fengpeng'


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str(self.start) + "-" + str(self.end)

    def __repr__(self):
        return str(self.start) + "-" + str(self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        res = [intervals[0]]
        for interval in intervals[1:]:
            last = res[-1]
            if last.end < interval.start:
                res.append(interval)
            else:
                last.end = max(last.end, interval.end)
        return res

i1 = Interval(1, 4)
i2 = Interval(0, 4)

intervals=[i1, i2]

print Solution().merge(intervals)