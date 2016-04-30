import sys

__author__ = 'fengpeng'


class Solution(object):
    def myAtoi(self, str):
        str = str.strip()
        if not str:
            return 0
        i = 0
        sign = 1
        res = 0
        MAX_INT = (1 << 31) - 1
        if str[i] == '-':
            sign = -1
            i += 1
        elif str[i] == '+':
            i += 1
        while i < len(str):
            if str[i] < '0' or str[i] > '9':
                break
            res = res * 10 + int(str[i])
            if res > sys.maxint:
                break
            i += 1
        res *= sign
        if res >= MAX_INT:
            return MAX_INT
        if res < -MAX_INT:
            return -MAX_INT - 1
        return res




