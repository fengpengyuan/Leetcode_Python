__author__ = 'fengpeng'


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k<=0:
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
        res.append(nums[que[0]]) # append the last one
        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
print Solution().maxSlidingWindow(nums, 4)



