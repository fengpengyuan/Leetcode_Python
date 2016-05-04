__author__ = 'fengpeng'


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) < 4:
            return res
        nums.sort()
        for i in xrange(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in xrange(i + 1, len(nums) - 2):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        beg, end = j + 1, len(nums) - 1
                        while beg < end:
                            s = nums[i] + nums[j] + nums[beg] + nums[end]
                            if s == target:
                                sol = [nums[i], nums[j], nums[beg], nums[end]]
                                res.append(sol)
                                beg += 1
                                end -= 1
                                while beg < end and nums[beg] == nums[beg - 1]:
                                    beg += 1
                                while beg < end and nums[end] == nums[end + 1]:
                                    end -= 1
                            elif s < target:
                                while beg < end and nums[beg] == nums[beg + 1]:
                                    beg += 1
                                beg += 1
                            else:
                                while beg < end and nums[end] == nums[end - 1]:
                                    end -= 1
                                end -= 1
        return res

    def fourSum2(self, num, target):
        res, dic = set(), {}
        if len(nums) < 4:
            return []
        nums.sort()
        for i in xrange(len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                s = nums[i] + nums[j]
                if s not in dic:
                    dic[s] = [(i, j)]
                else:
                    dic[s].append((i, j))
        for i in xrange(len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                left = target - nums[i] - nums[j]
                if left in dic:
                    for t in dic[left]:
                        if t[0] > j:
                            res.add((nums[i], nums[j], nums[t[0]], nums[t[1]]))
        return [list(i) for i in res]


nums = [1, 0, -1, 0, -2, 2]

print Solution().fourSum2(nums, 0)