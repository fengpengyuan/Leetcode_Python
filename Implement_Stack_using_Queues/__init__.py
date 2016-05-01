__author__ = 'fengpeng'


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1, self.q2 = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.top()
        self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1

    def top(self):
        """
        :rtype: int
        """
        while len(self.q1) > 1:
            tmp = self.q1.pop(0)
            self.q2.append(tmp)
        return self.q1[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.q1 and not self.q2


stk = Stack()
stk.push(1)

print stk.top()

