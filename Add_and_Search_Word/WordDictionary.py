__author__ = 'fengpeng'


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isLeaf = False


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            child = node.children.get(c)
            if child is None:
                child = TrieNode()
                node.children[c] = child
            node = child
        node.isLeaf = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchUtil(self.root, word, 0)

    def searchUtil(self, node, word, cur):
        # if (not node) or (cur == len(word) and not node.isLeaf):
        # return False
        # if cur == len(word) and node.isLeaf:
        #     return True
        if cur == len(word):
            return node.isLeaf
        c = word[cur]
        if c == '.':
            for x in node.children:
                res = self.searchUtil(node.children[x], word, cur + 1)
                if res:
                    return True
            return False
        else:
            child = node.children.get(c)
            if child is None:
                return False
            return self.searchUtil(child, word, cur + 1)


    #  solution  2
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchUtil(self.root, word)

    def searchUtil(self, node, word):
        if word=='':
            return node.isLeaf
        c = word[0]
        if c == '.':
            for x in node.children:
                res = self.searchUtil(node.children[x], word[1:])
                if res:
                    return True
        else:
            child = node.children.get(c)
            if child:
                return self.searchUtil(child, word[1:])
        return False


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("a")
wordDictionary.search(".")