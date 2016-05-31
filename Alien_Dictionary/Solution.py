import collections

__author__ = 'fengpeng'


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        map = collections.defaultdict(set)
        degree = collections.defaultdict(int)
        for word in words:
            for c in word:
                degree[c] = 0
        for i in xrange(1, len(words)):
            cur, pre = words[i], words[i - 1]
            for k in xrange(min(len(cur), len(pre))):
                c1, c2 = pre[k], cur[k]
                if c1 != c2:
                    map[c1].add(c2)
                    degree[c2] += 1
                    break
        res = ""
        que = []
        for c in degree:
            if degree[c] == 0:
                que.append(c)
        while que:
            ch = que.pop(0)
            res += ch
            for c in map[ch]:
                degree[c] -= 1
                if degree[c] == 0:
                    que.append(c)
        if len(res) == len(degree):
            return res
        return ""

    def alienOrderDFS(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        map = collections.defaultdict(set)
        visited = collections.defaultdict(int)
        for word in words:
            for c in word:
                visited[c] = 0
        for i in xrange(1, len(words)):
            cur, pre = words[i], words[i - 1]
            for k in xrange(min(len(cur), len(pre))):
                c1, c2 = pre[k], cur[k]
                if c1 != c2:
                    map[c1].add(c2)
                    break

        res = []
        for c in map.keys():
            if self.detectCycle(c, map, visited, res):
                return ""
        return "".join(res)

    def detectCycle(self, c, map, visited, res):
        if visited[c] == -1:
            return True
        if visited[c] == 1:
            return False
        visited[c] = -1
        for c1 in map[c]:
            if self.detectCycle(c1, map, visited, res):
                return True
        visited[c] = 1
        res.insert(0, c)
        return False


words = [
    "caa", "aaa", "aab"
]

print Solution().alienOrder(words)

print Solution().alienOrderDFS(words)




