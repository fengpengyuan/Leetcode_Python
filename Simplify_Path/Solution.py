__author__ = 'fengpeng'


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ps = path.split("/")
        stk = []

        print ps
        for s in ps:
            if s == '.' or s == '':
                continue
            if s == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(s)
        if not stk:
            return "/"
        res = ""
        for p in stk:
            res += "/" + p
        return res


print Solution().simplifyPath("/home//foo/")


