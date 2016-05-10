__author__ = 'fengpeng'


class Solution(object):
    # the condition A[left] == A[mid] holds true, which leaves us with only two possibilities:
    # All numbers between A[left] and A[right] are all 1's.
    # Different numbers (including our target) may exist between A[left] and A[right].
    # As we cannot determine which of the above is true,
    # the best we can do is to move left one step to the right and repeat the process again.
    # Therefore, we are able to construct a worst case input which runs in O(n)
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) / 2
            if nums[m] == target:
                return True
            if nums[m] > nums[i]:
                if nums[i] <= target < nums[m]:
                    j = m - 1
                else:
                    i = m + 1
            elif nums[m] < nums[i]:
                if nums[m] < target <= nums[j]:
                    i = m + 1
                else:
                    j = m - 1
            else:
                i += 1
        return False
