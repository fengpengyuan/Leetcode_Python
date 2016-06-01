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
        # (m + n) / 2 + 1)) / 2.0
        # else:
        # return self.findKth(nums1, 0, nums2, 0, (m + n) / 2)

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

    def findMedianSortedArrays2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m>n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax, halfLen = 0, m, (m + n + 1) / 2

        while imin <= imax:
            i = (imin + imax) / 2
            j = halfLen - i

            if i > 0 and j < n and nums1[i - 1] > nums2[j]:
                imax = i - 1
            elif j > 0 and i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            else:
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2.0


nums1 = [6]
nums2 = []

# 1 2 3 4 5 6 7 8 9 10

print Solution().findMedianSortedArrays(nums1, nums2)
print Solution().findMedianSortedArrays2(nums1, nums2)