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

    def convert2(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        rows = [""] * numRows
        down, row = True, 0
        for i in xrange(len(s)):
            rows[row] += s[i]
            if row == numRows - 1:
                down = False
            elif row==0:
                down = True
            if down:
                row += 1
            else:
                row -= 1
        return "".join(rows)


print Solution().convert("PAYPALISHIRING", 3)
print Solution().convert2("ABC", 1)

