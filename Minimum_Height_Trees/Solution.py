__author__ = 'fengpeng'


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        nodes = [[] for _ in xrange(n)]
        for edge in edges:
            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0])
        leaves = []
        for i in xrange(len(nodes)):
            if len(nodes[i]) == 1:
                leaves.append(i)
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for leaf in leaves:
                nodes[nodes[leaf][0]].remove(leaf)
                if len(nodes[nodes[leaf][0]]) == 1:
                    newLeaves.append(nodes[leaf][0])
            leaves = newLeaves
        return leaves

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        adj = [set() for _ in xrange(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in xrange(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves


n = 4
edges = [[1, 0], [1, 2], [1, 3]]

print Solution().findMinHeightTrees(n, edges)
