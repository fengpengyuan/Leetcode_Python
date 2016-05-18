__author__ = 'fengpeng'


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = set(nums1)
        res = set()
        for num in nums2:
            if num in s1:
                res.add(num)
        return [i for i in res]

nums1=[1, 1]
nums2=[1]

print Solution().intersection(nums1, nums2)