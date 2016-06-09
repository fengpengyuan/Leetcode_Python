__author__ = 'fengpeng'


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls, cows = 0, 0
        s, g = [0] * 10, [0] * 10

        for c1, c2 in zip(secret, guess):
            if c1 == c2:
                bulls += 1
            else:
                s[int(c1)] += 1
                g[int(c2)] += 1
        for i1, i2 in zip(s, g):
            cows += min(i1, i2)
        return str(bulls) + 'A' + str(cows) + 'B'

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls, cows = 0, 0
        numbers = [0] * 10

        for i in xrange(len(secret)):
            s, g = secret[i], guess[i]
            if s == g:
                bulls += 1
            else:
                if numbers[int(s)] < 0:
                    cows += 1
                if numbers[int(g)] > 0:
                    cows += 1
                numbers[int(s)] += 1
                numbers[int(g)] -= 1
        return str(bulls) + 'A' + str(cows) + 'B'


print Solution().getHint("1123", "0111")