__author__ = 'fengpeng'


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, word, 0, visited):
                        return True
        return False

    def dfs(self, board, i, j, word, cur, visited):
        if cur == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
            return False
        visited[i][j] = True
        res = self.dfs(board, i + 1, j, word, cur + 1, visited) or \
            self.dfs(board, i - 1, j, word, cur + 1, visited) or \
            self.dfs(board, i, j - 1, word, cur + 1, visited) or \
            self.dfs(board, i, j + 1, word, cur + 1, visited)
        if res:
            return True
        visited[i][j] = False
        return False


board = ["b","a","b"]

print Solution().exist(board, "bbabab")