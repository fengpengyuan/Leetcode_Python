__author__ = 'fengpeng'


class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return dic.get(target - nums[i]), i
            dic[nums[i]] = i

    def twoSum2(self, nums, target):
        dic = {}
        for i, elem in enumerate(nums):
            if target - elem in dic:
                return dic.get(target - elem), i
            dic[elem] = i


numbers = [2, 7, 11, 15]
print(Solution().twoSum(numbers, 9))
