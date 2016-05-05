__author__ = 'fengpeng'


class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.it = []
        if v1:
            self.it.append(v1)
        if v2:
            self.it.append(v2)

    def next(self):
        """
        :rtype: int
        """
        v = self.it.pop(0)
        res = v.pop(0)
        if v:
            self.it.append(v)
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.it) != 0

    ##############################################
    # solution 2
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2

    def next(self):
        """
        :rtype: int
        """
        if self.v1:
            res = self.v1.pop(0)
            self.v1, self.v2 = self.v2, self.v1
            return res
        else:
            res = self.v2.pop(0)
            return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.v1) + len(self.v2) > 0

    ##########################
    # solution 3
    # there is no hasnext method for iterator in python, it stops by raising a exception
    # def __init__(self, v1, v2):
    #     """
    #     Initialize your data structure here.
    #     :type v1: List[int]
    #     :type v2: List[int]
    #     """
    #     self.it = []
    #     if v1:
    #         self.it.append(iter(v1))
    #     if v2:
    #         self.it.append(iter(v2))
    #
    # def next(self):
    #     """
    #     :rtype: int
    #     """
    #     v = self.it.pop(0)
    #     res = v.next()
    #     if v.hasNext():
    #         self.it.append(v)
    #     return res
    #
    # def hasNext(self):
    #     """
    #     :rtype: bool
    #     """
    #     return len(self.it) != 0

# Your ZigzagIterator object will be instantiated and called as such:
v1 = [1, 2, 3]
v2 = [4, 5, 6]
i, v = ZigzagIterator(v1, v2), []
while i.hasNext():
    v.append(i.next())
print v