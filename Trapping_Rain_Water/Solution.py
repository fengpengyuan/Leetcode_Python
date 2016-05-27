__author__ = 'fengpeng'


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 3:
            return 0
        left, right = [0] * n, [0] * n
        m = height[0]
        for i in xrange(1, n):
            m = max(m, height[i])
            left[i] = m
        m = height[n - 1]
        for i in xrange(n - 2, -1, -1):
            m = max(m, height[i])
            right[i] = m
        res = 0
        for i in xrange(n):
            m = min(left[i], right[i])
            if m >= height[i]:
                res += m - height[i]
        return res

    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 3:
            return 0
        dp = [0] * n
        m = 0
        for i in xrange(n):
            m = max(m, height[i])
            dp[i] = m
        m, res = 0, 0
        for i in xrange(n - 1, -1, -1):
            m = max(m, height[i])
            dp[i] = min(dp[i], m)
            if dp[i] > height[i]:
                res += dp[i] - height[i]
        return res

    def trap3(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left, right = 0, n - 1
        leftMax, rightMax = 0, 0
        res = 0
        while left <= right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if leftMax < rightMax:
                res += leftMax - height[left]
                left += 1
            else:
                res += rightMax - height[right]
                right -= 1
        return res


water = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print Solution().trap(water)

print Solution().trap2(water)
print Solution().trap3(water)
