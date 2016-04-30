__author__ = 'fengpeng'


class Solution(object):
    def numIslands(self, grid):
        n = len(grid)
        if n == 0:
            return 0
        count = 0
        for i in range(n):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


    def numIslandsBFS(self, grid):
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        que = []
        count = 0
        # visited=[[False for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    grid[i][j] = '#'
                    count += 1
                    que.append([i, j])
                    while que:
                        [x, y] = que.pop(0)
                        if x - 1 >= 0 and grid[x - 1][y] == '1':
                            que.append([x - 1, y])
                            grid[x - 1][y] = '#'
                        if x + 1 < n and grid[x + 1][y] == '1':
                            que.append([x + 1, y])
                            grid[x + 1][y] = '#'
                        if y - 1 >= 0 and grid[x][y - 1] == '1':
                            que.append([x, y - 1])
                            grid[x][y - 1] = '#'
                        if y + 1 < m and grid[x][y + 1] == '1':
                            que.append([x, y + 1])
                            grid[x][y + 1] = '#'
        return count






