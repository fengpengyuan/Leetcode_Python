import collections
import heapq

__author__ = 'fengpeng'


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k <= 0:
            return []
        res, que = [], []
        for i in xrange(k):
            while que and nums[i] > nums[que[-1]]:
                que.pop()
            que.append(i)
        for i in xrange(k, len(nums)):
            res.append(nums[que[0]])
            if i - k >= que[0]:
                que.pop(0)
            while que and nums[i] > nums[que[-1]]:
                que.pop()
            que.append(i)
        res.append(nums[que[0]])  # append the last one
        return res

    def maxSlidingWindow2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = collections.deque()
        res = []
        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)
            if i - dq[0] == k:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res

    def maxSlidingWindow3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k <= 0:
            return []
        res, heap = [], []
        for i, num in enumerate(nums):
            if len(heap) < k:
                heapq.heappush(heap, (-num, i))
            else:
                res.append(-heap[0][0])
                while heap and heap[0][1] <= i - k:
                    heapq.heappop(heap)
                heapq.heappush(heap, (-num, i))
        res.append(-heap[0][0])
        return res

    def maxSlidingWindow4(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq, res = collections.deque(), []
        for i, num in enumerate(nums):
            while dq and dq[-1] < num:
                dq.popleft()
            dq.append(num)
            if i >= k and dq[0] == nums[i - k]:
                dq.popleft()
            if i >= k - 1:
                res.append(dq[0])
        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
nums2 = [1, 3, -1, -3, 5, 3, 6, 7]
print Solution().maxSlidingWindow2(nums, 4)
print Solution().maxSlidingWindow3(nums2, 4)
print Solution().maxSlidingWindow4(nums2, 4)



