__author__ = 'fengpeng'


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str(self.start) + "-" + str(self.end)


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        inserted = False
        for interval in intervals:
            if interval.start < newInterval.start or inserted:
                self.insertInterval(res, interval)
            else:
                self.insertInterval(res, newInterval)
                inserted = True
                self.insertInterval(res, interval)
        if not inserted:
            self.insertInterval(res, newInterval)
        return res

    def insert2(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        inserted = False
        for interval in intervals:
            if newInterval.start < interval.start and not inserted:
                inserted = True
                self.insertInterval(res, newInterval)
            self.insertInterval(res, interval)
        if not inserted:
            self.insertInterval(res, newInterval)
        print res[0]
        return res


    def insertInterval(self, res, interval):
        if not res:
            res.append(interval)
        else:
            pre = res[-1]
            if pre.end < interval.start:
                res.append(interval)
            else:
                pre.end = max(pre.end, interval.end)


i1 = Interval(1, 5)
# i2 = Interval(3, 5)
# i3 = Interval(6, 7)
# i4 = Interval(8, 10)
# i5 = Interval(12, 16)

# intervals = [i1, i2, i3, i4, i5]
intervals = [i1]
newInterval = Interval(2, 3)

print Solution().insert(intervals, newInterval)
