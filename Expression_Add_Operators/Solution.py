__author__ = 'fengpeng'


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        self.dfs(num, target, res, "", 0, 0, 0)
        return res

    def dfs(self, nums, target, res, sol, pos, cur, pre):
        if pos == len(nums) and cur == target:
            res.append(sol)
            return
        for i in xrange(pos, len(nums)):
            if i!=pos and nums[pos]=='0':
                break
            s = "".join(nums[pos:i + 1])
            # if len(s) > 1 and s[0] == '0':
            #     return
            num = int(s)
            if pos == 0:
                self.dfs(nums, target, res, str(num), i + 1, num, num)
            else:
                self.dfs(nums, target, res, sol + "+" + str(num), i + 1, cur + num, num)
                self.dfs(nums, target, res, sol + '-' + str(num), i + 1, cur - num, -num)
                self.dfs(nums, target, res, sol + "*" + str(num), i + 1, cur - pre + pre * num, pre * num)


print Solution().addOperators("105", 5)