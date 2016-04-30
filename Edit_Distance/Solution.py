__author__ = 'fengpeng'


class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        # dp = [[0] * (n+1) for j in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j],#insert
                                   dp[i][j - 1],#delete
                                   dp[i - 1][j - 1]) + 1#replace

        return dp[m][n]


        # m=len(word1)+1; n=len(word2)+1
        # dp = [[0 for i in range(n)] for j in range(m)]
        # for i in range(n):
        #     dp[0][i]=i
        # for i in range(m):
        #     dp[i][0]=i
        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(0 if word1[i-1]==word2[j-1] else 1))
        # return dp[m-1][n-1]


w, h = 5, 8
Matrix = [[0 for x in range(w)] for y in range(h)]
print(Matrix)

Solution().minDistance("", "")