__author__ = 'fengpeng'


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        # base case first
        # if input.find("+") == -1 and input.find("-") == -1 and input.find("*") == -1:
        # res.append(int(input))
        #     return res

        for i in xrange(len(input)):
            c = input[i]
            if c == '+' or c == '-' or c == '*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])

                for v1 in left:
                    for v2 in right:
                        if c == '+':
                            res.append(v1 + v2)
                        elif c == '-':
                            res.append(v1 - v2)
                        else:
                            res.append(v1 * v2)
        # base case here
        if not res:
            res.append(int(input))
        return res


    def diffWaysToCompute2(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        dict = {}
        return self.helper(input, dict)

    def helper(self, s, dict):
        # if not s:
        #     return []
        if s in dict:
            return dict[s]
        res = []
        for i in xrange(len(s)):
            c = s[i]
            if c == '+' or c == '-' or c == '*':
                s1 = s[:i]
                s2 = s[i + 1:]
                res1, res2 = [], []
                if s1 in dict:
                    res1 = dict[s1]
                else:
                    res1 = self.helper(s1, dict)
                if s2 in dict:
                    res2 = dict[s2]
                else:
                    res2 = self.helper(s2, dict)

                for v1 in res1:
                    for v2 in res2:
                        if c == '+':
                            res.append(v1 + v2)
                        elif c == '-':
                            res.append(v1 - v2)
                        else:
                            res.append(v1 * v2)
        if not res:
            res.append(int(s))
        dict[input] = res
        return res


input = "2-1-1"

print Solution().diffWaysToCompute(input)
print Solution().diffWaysToCompute2(input)