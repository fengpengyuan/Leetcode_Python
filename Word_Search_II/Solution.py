__author__ = 'fengpeng'


class TrieNode(object):
    def __init__(self):
        self.isLeaf = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isLeaf = True

    def search(self, word):
        cur = self.root
        for c in word:
            if not cur or c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isLeaf

    def startWith(self, prefix):
        cur = self.root
        for c in prefix:
            if not cur or c not in cur.children:
                return False
            cur = cur.children[c]
        return True


class Solution(object):
    # def findWords(self, board, words):
    # """
    # :type board: List[List[str]]
    #     :type words: List[str]
    #     :rtype: List[str]
    #     """
    #     dict = set(words)
    #     res = set()
    #     m, n = len(board), len(board[0])
    #     visited = [[False] * n for _ in xrange(m)]
    #     for i in xrange(m):
    #         for j in xrange(n):
    #             self.dfs(board, i, j, dict, "", visited, res)
    #     return list(res)
    #
    # def dfs(self, board, i, j, dict, word, visited, res):
    #     if word in dict:
    #         res.add(word)
    #
    #     if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
    #         return
    #     visited[i][j] = True
    #     self.dfs(board, i + 1, j, dict, word + board[i][j], visited, res)
    #     self.dfs(board, i - 1, j, dict, word + board[i][j], visited, res)
    #     self.dfs(board, i, j + 1, dict, word + board[i][j], visited, res)
    #     self.dfs(board, i, j - 1, dict, word + board[i][j], visited, res)
    #     visited[i][j] = False

    def findWords2(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in xrange(m)]
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = set()
        for i in xrange(m):
            for j in xrange(n):
                self.dfs(board, trie.root, i, j, "", visited, res)
        return list(res)

    def dfs(self, board, trie, i, j, word, visited, res):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
            return
        if board[i][j] not in trie.children:
            return
        trie = trie.children[board[i][j]]
        word += board[i][j]
        if trie.isLeaf:
            res.add(word)
        visited[i][j] = True
        self.dfs(board, trie, i + 1, j, word, visited, res)
        self.dfs(board, trie, i - 1, j, word, visited, res)
        self.dfs(board, trie, i, j + 1, word, visited, res)
        self.dfs(board, trie, i, j - 1, word, visited, res)
        visited[i][j] = False


board = [list("bbaaba"), list("bbabaa"), list("bbbbbb"), list("aaabaa"), list("abaabb")]

words = ["abbbababaa"]

trie = Trie()
trie.insert("oath")

print trie.search("oath")

print list("abc")

print Solution().findWords2(board, words)