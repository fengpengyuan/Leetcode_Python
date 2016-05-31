__author__ = 'fengpeng'


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # if "mid + 1" is a valid h index,
        # it means value of position "citationsSize - mid - 1" must exceed "mid"
        n = len(citations)
        i, j = 0, n - 1

        while i <= j:
            mid = (i + j) / 2
            if citations[n - mid - 1] > mid:
                i = mid + 1
            else:
                j = mid - 1
        return i


A = [0, 1, 3, 4, 5, 6]

print Solution().hIndex(A)