__author__ = 'fengpeng'


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.isLeaf = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    # def insert(self, word):
    #     """
    #     Inserts a word into the trie.
    #     :type word: str
    #     :rtype: void
    #     """
    #     node = self.root
    #     for c in word:
    #         if c in node.map:
    #             node = node.map.get(c)
    #         else:
    #             newNode = TrieNode()
    #             node.map[c] = newNode
    #             node = newNode
    #     node.isLeaf = True
    #
    # def search(self, word):
    #     """
    #     Returns if the word is in the trie.
    #     :type word: str
    #     :rtype: bool
    #     """
    #     node = self.root
    #     for c in word:
    #         children = node.map
    #         if c in children:
    #             node = children[c]
    #         else:
    #             return False
    #     return node.isLeaf
    #
    # def startsWith(self, prefix):
    #     """
    #     Returns if there is any word in the trie
    #     that starts with the given prefix.
    #     :type prefix: str
    #     :rtype: bool
    #     """
    #     node = self.root
    #     for c in prefix:
    #         children = node.map
    #         if c in children:
    #             node = children[c]
    #         else:
    #             return False
    #     return True

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            child = node.map.get(c)
            if not child:
                child = TrieNode()
                node.map[c] = child
            node = child

        node.isLeaf = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            children = node.map
            node = children.get(c)
            if node is None:
                return False
        return node.isLeaf

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            children = node.map
            node = children.get(c)
            if node is None:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")