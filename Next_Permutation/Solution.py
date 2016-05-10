__author__ = 'fengpeng'


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = -1
        for i in xrange(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                index = i
        if index == -1:
            nums.sort()
            return

        idx = index + 1
        for j in xrange(index + 1, len(nums)):
            if nums[j] > nums[index]:
                idx = j
        nums[index], nums[idx] = nums[idx], nums[index]
        right = nums[index + 1:]
        right.sort()
        nums[index + 1:] = right
        # nums[index+1:].sort()
        # i, j = index + 1, len(nums) - 1
        # while i < j:
        # nums[i], nums[j] = nums[j], nums[i]
        # i += 1
        # j -= 1


        # nums = nums[:index+1] + right does not work
        #when you do this:
        # num = num[:pre]+tmp
        # actually you did not modify the array which num referrer, you just assign a new array referrer to num, that means you did not modify the old array the question given to you.
        #
        # try this
        #
        # num[pre+1:]=tmp


nums = [1, 3, 2]

Solution().nextPermutation(nums)
