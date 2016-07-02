__author__ = 'fengpeng'


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        used = [False] * len(nums)
        self.helper(nums, 0, used, [], res)
        return res

    def helper(self, nums, cur, used, sol, res):
        res.append(list(sol))
        if cur == len(nums):
            return
        for i in xrange(cur, len(nums)):
            if not used[i]:
                if i != 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                sol.append(nums[i])
                used[i] = True
                self.helper(nums, i + 1, used, sol, res)
                sol.pop()
                used[i] = False


    def subsetsWithDup2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        i = 0
        while i < len(nums):
            dupCount = 0
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                dupCount += 1
                i += 1
            preSize = len(res)
            print preSize
            print res
            for j in xrange(preSize):
                element = list(res[j])
                for k in xrange(dupCount + 1):
                    element.append(nums[i])
                    res.append(list(element))
            i += 1
        return res

    def subsetsWithDup3(self, nums):
        nums.sort()

        return self.subsetHelper(nums)

    def subsetHelper(self, nums):
        if not nums:
            return [[]]
        res = [[]]
        for i, e in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            rest_subsets=self.subsetHelper(nums[i+1:])
            for subset in rest_subsets:
                subset.insert(0, e)
            res+=rest_subsets
        return res



nums = [1, 2, 2]

print Solution().subsetsWithDup(nums)
print Solution().subsetsWithDup2(nums)
print Solution().subsetsWithDup3(nums)