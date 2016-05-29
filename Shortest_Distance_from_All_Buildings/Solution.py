import sys

__author__ = 'fengpeng'


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: matrix
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        buildingNum = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        distance, reach = [[0] * n for _ in xrange(m)], [[0] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    buildingNum += 1
                    visited = [[False] * n for _ in xrange(m)]
                    que = list()
                    que.append((i, j))
                    level = 1

                    while que:
                        size = len(que)
                        for q in xrange(size):
                            first = que.pop(0)
                            for k in xrange(4):
                                x = first[0] + dirs[k][0]
                                y = first[1] + dirs[k][1]
                                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and not visited[x][y]:
                                    visited[x][y] = True
                                    distance[x][y] += level
                                    reach[x][y] += 1
                                    que.append((x, y))
                        level += 1

        res = sys.maxint
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 0 and reach[i][j] == buildingNum:
                    res = min(res, distance[i][j])
        return -1 if res == sys.maxint else res


grid = [[1, 0, 2, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]]

print Solution().shortestDistance(grid)
