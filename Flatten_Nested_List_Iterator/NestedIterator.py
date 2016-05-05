__author__ = 'fengpeng'


class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stk = []
        for i in xrange(len(nestedList) - 1, -1, -1):
            self.stk.append(nestedList[i])

    def next(self):
        """
        :rtype: int
        """
        return self.stk.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stk:
            top = self.stk[-1]
            if top.isInteger():
                return True
            else:
                top = self.stk.pop()
                lst = top.getList()
                for i in xrange(len(lst) - 1, -1, -1):
                    self.stk.append(lst[i])
        return False
