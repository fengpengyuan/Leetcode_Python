__author__ = 'fengpeng'


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        index = 0
        citations = sorted(citations, reverse=True)
        for i in xrange(len(citations)):
            if citations[i] >= i + 1:
                index = i + 1
        return index

    def hIndex2(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        stats = [0] * (n + 1)

        for citation in citations:
            if citation >= n:
                stats[n] += 1
            else:
                stats[citation] += 1
        sum = 0
        for i in xrange(n, -1, -1):
            sum += stats[i]
            if sum >= i:
                return i
        return 0


citations = [3, 0, 6, 1, 5]

print Solution().hIndex(citations)
print Solution().hIndex2(citations)