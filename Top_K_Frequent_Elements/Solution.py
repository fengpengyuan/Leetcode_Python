import heapq

__author__ = 'fengpeng'


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or len(nums) < k:
            return []
        res, heap, dic = [], [], {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1

        for key, val in dic.iteritems():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                if heapq.nsmallest(1, heap)[0][0] < val:
                    heapq.heappushpop(heap, (val, key))
        while heap:
            res.append(heap.pop()[1])
        return res


nums = [4, 1, -1, 2, -1, 2, 3]

print Solution().topKFrequent(nums, 2)


