__author__ = 'fengpeng'


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 0-dead to dead
        # 1-live to live
        # 2-live to dead
        # 3-dead to live
        di = [-1, -1, -1, 0, 0, 1, 1, 1]
        dj = [-1, 0, 1, -1, 1, -1, 0, 1]

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                live = 0
                for k in xrange(8):
                    ii, jj = i + di[k], j + dj[k]
                    if ii < 0 or jj < 0 or ii >= len(board) or jj >= len(board[0]):
                        continue
                    if board[ii][jj] == 1 or board[ii][jj] == 2:
                        live += 1

                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = 2
                if board[i][j] == 0 and live == 3:
                    board[i][j] = 3

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                board[i][j] %= 2

