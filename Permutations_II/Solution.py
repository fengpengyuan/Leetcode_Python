__author__ = 'fengpeng'


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, perm = [], []
        nums.sort()
        visited = set()
        self.permuteUniqueUtil(nums, res, perm, visited)
        return res

    def permuteUniqueUtil(self, nums, res, perm, visited):
        if len(perm) == len(nums):
            res.append(perm + [])
            return
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1] and i - 1 not in visited:
                continue
            if i not in visited:
                perm.append(nums[i])
                visited.add(i)
                self.permuteUniqueUtil(nums, res, perm, visited)
                perm.pop()
                visited.remove(i)


    # use array instead of set
    def permuteUnique(self, nums):
        res, sol = [], []
        nums.sort()
        used = [False] * len(nums)

        self.permute(nums, res, sol, used)
        return res

    def permute(self, nums, res, sol, used):
        if len(sol) == len(nums):
            res.append(list(sol))

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            if not used[i]:
                used[i] = True
                sol.append(nums[i])
                self.permute(nums, res, sol, used)
                sol.pop()
                used[i] = False

    # solution 2
    def permuteUnique2(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        nums.sort()
        res, pre = [], None
        for i in range(len(nums)):
            if nums[i] == pre:
                continue
            pre = nums[i]
            for j in self.permuteUnique2(nums[:i] + nums[i + 1:]):
                res.append([nums[i]]+j)
        return res


nums = [1, 2, 1]

print Solution().permuteUnique2(nums)