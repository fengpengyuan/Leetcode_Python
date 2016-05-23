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
        #     res.append(int(input))
        #     return res

        for i in xrange(len(input)):
            c = input[i]
            if c == '+' or c == '-' or c == '*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                print "left:", left
                print "right: ", right
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


input = "2-1-1"

print Solution().diffWaysToCompute(input)