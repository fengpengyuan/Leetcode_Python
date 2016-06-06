__author__ = 'fengpeng'


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            rows = [False] * 10
            cols = [False] * 10
            for j in xrange(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if 1 <= num <= 9:
                        if rows[num]:
                            return False
                        rows[num] = True
                if board[j][i] != '.':
                    num = int(board[j][i])
                    if 1 <= num <= 9:
                        if cols[num]:
                            return False
                        cols[num] = True
        for i in xrange(0, 9, 3):
            for j in xrange(0, 9, 3):
                grid = [False] * 10
                for k in xrange(3):
                    for l in xrange(3):
                        if board[i + k][j + l] != '.':
                            num = int(board[i + k][j + l])
                            if 1 <= num <= 9:
                                if grid[num]:
                                    return False
                                grid[num] = True
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[0] * 9 for _ in xrange(9)]
        cols = [[0] * 9 for _ in xrange(9)]
        grid = [[0] * 9 for _ in xrange(9)]

        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    k = i / 3 * 3 + j / 3
                    if rows[i][num] or cols[j][num] or grid[k][num]:
                        return False
                    rows[i][num] = cols[j][num] = grid[k][num] = 1
        return True
