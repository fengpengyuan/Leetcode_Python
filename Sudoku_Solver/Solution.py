__author__ = 'fengpeng'


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        empty = []
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    empty.append((i, j))
        self.dfs(board, empty, 0)

    def dfs(self, board, empty, cur):
        if cur == len(empty):
            return True
        row = empty[cur][0]
        col = empty[cur][1]
        for i in xrange(1, 10):
            if self.isValidSudoku(board, row, col, str(i)):
                board[row][col] = str(i)
                if self.dfs(board, empty, cur + 1):
                    return True
                board[row][col] = '.'
        return False

    def isValidSudoku(self, board, row, col, val):
        for i in xrange(9):
            if board[row][i] == val:
                return False
            if board[i][col] == val:
                return False
            sub_row = row / 3 * 3 + i / 3
            sub_col = col / 3 * 3 + i % 3
            if board[sub_row][sub_col] == val:
                return False
        # for i in xrange(3):
        #     for j in xrange(3):
        #         sub_row = row / 3 * 3 + i
        #         sub_col = col / 3 * 3 + j
        #         # print board[sub_row][sub_col], val
        #         if board[sub_row][sub_col] == val:
        #             return False
        return True

    def solveSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.solver(board)

    def solver(self, board):
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    for v in xrange(1, 10):
                        if self.isValidSudoku(board, i, j, str(v)):
                            a = list(board[i])
                            a[j] = str(v)
                            board[i] = ''.join(a)
                            if self.solver(board):
                                return True
                            else:
                                a[j] = '.'
                                board[i] = ''.join(a)
                    return False
        return True


grid = [["53..7...."], ["6..195..."], [".98....6."], ["8...6...3"], ["4..8.3..1"], ["7...2...6"], [".6....28."],
        ["...419..5"], ["....8..79"]]
board = []
for x in xrange(9):
    board.append(list(grid[x][0]))
print board

Solution().solveSudoku(board)
print board

