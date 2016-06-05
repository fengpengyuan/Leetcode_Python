__author__ = 'fengpeng'


class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.row = 0
        self.col = 0
        self.vec = vec2d

    def next(self):
        res = self.vec[self.row][self.col]
        self.col += 1
        return res

    def hasNext(self):
        while self.row < len(self.vec):
            if self.col < len(self.vec[self.row]):
                return True
            self.row += 1
            self.col = 0
        return False


vector =[
  [1,2],
  [3],
  [4,5,6]
]

i, v = Vector2D(vector), []
while i.hasNext():
    v.append(i.next())

print v
