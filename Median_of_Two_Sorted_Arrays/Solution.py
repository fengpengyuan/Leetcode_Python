import sys

__author__ = 'fengpeng'


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        l = (m + n + 1) / 2
        r = (m + n + 2) / 2

        return (self.findKth(nums1, 0, nums2, 0, l) + self.findKth(nums1, 0, nums2, 0, r)) / 2.0
        # if (m + n) % 2 == 0:
        # return (self.findKth(nums1, 0, nums2, 0, (m + n) / 2) + self.findKth(nums1, 0, nums2, 0,
        #                                                                          (m + n) / 2 + 1)) / 2.0
        # else:
        #     return self.findKth(nums1, 0, nums2, 0, (m + n) / 2)

    def findKth(self, nums1, s1, nums2, s2, k):
        if s1 >= len(nums1):
            return nums2[s2 + k - 1]
        if s2 >= len(nums2):
            return nums1[s1 + k - 1]
        if k == 1:
            return min(nums1[s1], nums2[s2])
        mid1, mid2 = sys.maxint, sys.maxint
        if s1 + k / 2 - 1 < len(nums1):
            mid1 = nums1[s1 + k / 2 - 1]
        if s2 + k / 2 - 1 < len(nums2):
            mid2 = nums2[s2 + k / 2 - 1]

        if mid1 < mid2:
            return self.findKth(nums1, s1 + k / 2, nums2, s2, k - k / 2)
        else:
            return self.findKth(nums1, s1, nums2, s2 + k / 2, k - k / 2)


nums1 = [5, 6, 7, 8]
nums2 = [1, 2, 3, 4, 5]

# 1 2 3 4 5 5 6 7 8

print Solution().findMedianSortedArrays(nums1, nums2)