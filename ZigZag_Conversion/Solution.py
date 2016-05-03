__author__ = 'fengpeng'


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) < numRows or numRows < 2:
            return s
        rows, row, down = [""] * numRows, 0, -1

        for c in s:
            rows[row] += c
            if row == numRows - 1 or row == 0:
                down *= -1
            row += down
        return "".join(rows)


print Solution().convert("PAYPALISHIRING", 3)

