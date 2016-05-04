__author__ = 'fengpeng'
'''
Given an array, print the Next Greater Element (NGE) for every element.
The Next greater Element for an element x is the first greater element on the right side of x in array.
Elements for which no greater element exist, consider next greater element as -1.
'''


class Solution(object):
    def nextGreaterElement(self, nums):
        stk = []
        for num in nums:
            while stk and stk[-1] < num:
                print str(stk.pop()) + '--->' + str(num)
            stk.append(num)
        while stk:
            print str(stk.pop()) + '--->' + str(-1)


nums = [2, 5, 1, 3, 7]

Solution().nextGreaterElement(nums)
