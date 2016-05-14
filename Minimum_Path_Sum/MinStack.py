__author__ = 'fengpeng'


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.min = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stk.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)


    def pop(self):
        """
        :rtype: void
        """
        e = self.stk.pop()
        if e==self.min[-1]:
            self.min.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()