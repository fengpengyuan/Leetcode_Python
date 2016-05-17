__author__ = 'fengpeng'


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for c in s:
            if not stk or c in ('(', '[', '{'):
                stk.append(c)
            else:
                if (c == '}' and stk[-1] == '{') or (c == ']' and stk[-1] == '[') or (c == ')' and stk[-1] == '('):
                    stk.pop()
                else:
                    return False
        return not stk