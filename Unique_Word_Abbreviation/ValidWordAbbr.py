import collections

__author__ = 'fengpeng'


class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.d = collections.defaultdict(list)
        for word in dictionary:
            k = word
            if len(word) > 2:
                k = word[0] + str(len(word) - 2) + word[-1]
            self.d[k].append(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abb = word[0] + str(len(word) - 2) + word[-1]

        return len(self.d[abb]) == 0 or len(self.d[abb]) == 1 and self.d[abb][0] == word


dictionary = ["deer", "door", "cake", "card"]

print ValidWordAbbr(dictionary).isUnique("dear")
print ValidWordAbbr(dictionary).isUnique("cart")
print ValidWordAbbr(dictionary).isUnique("cane")
print ValidWordAbbr(dictionary).isUnique("make")
