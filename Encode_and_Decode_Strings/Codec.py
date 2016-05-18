__author__ = 'fengpeng'


class Codec(object):
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(s):
            sharp = s.find("#", i)
            l = int("".join(s[i:sharp]))
            res.append(s[sharp + 1:sharp + 1 + l])
            i = sharp + l + 1
        return res


strs = ["i", "am", "a", "student"]

lst = Codec().encode(strs)
print lst

print Codec().decode(lst)