__author__ = 'fengpeng'


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.sum = 0
        self.q = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.q)>=self.size:
            self.sum -= self.q.pop(0)
        self.sum+=val
        self.q.append(val)
        return 1.0*self.sum/len(self.q)

# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
param_1 = obj.next(1)
print param_1
param_1 = obj.next(2)
print param_1
param_1 = obj.next(3)
print param_1
param_1 = obj.next(4)
print param_1

