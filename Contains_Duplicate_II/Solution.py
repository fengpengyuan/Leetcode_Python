__author__ = 'fengpeng'


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, num in enumerate(nums):
            print dic
            if num in dic:
                if i - dic[num] <= k:
                    return True

            dic[num] = i
        return False

nums=[1,2,1]

print Solution().containsNearbyDuplicate(nums, 0)