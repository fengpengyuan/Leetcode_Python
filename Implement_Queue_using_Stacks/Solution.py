__author__ = 'fengpeng'


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk1, self.stk2 = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stk1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        # if self.stk2:
        #     self.stk2.pop()
        # else:
        #     while self.stk1:
        #         self.stk2.append(self.stk1.pop())
        #     self.stk2.pop()

        # peek first then pop
        self.peek()
        self.stk2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.stk2:
            return self.stk2[-1]
        else:
            while self.stk1:
                self.stk2.append(self.stk1.pop())
            return self.stk2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stk1 and not self.stk2


q = Queue()
q.push(2)
q.push(3)
print q.peek()
q.pop()

q.push(5)

print q.empty()
print q.peek()