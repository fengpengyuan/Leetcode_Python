import heapq

__author__ = 'fengpeng'


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minHeap, self.maxHeap = [], []


    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.maxHeap, -num)
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        if len(self.maxHeap)<len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))


    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            return -self.maxHeap[0]



        # Your MedianFinder object will be instantiated and called as such:


mf = MedianFinder()
mf.addNum(1)
print mf.findMedian()
mf.addNum(2)
print mf.findMedian()
mf.addNum(3)
print mf.findMedian()
mf.addNum(4)
print mf.findMedian()
mf.addNum(5)
print mf.findMedian()

