__author__ = 'fengpeng'


# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return
        d = {}
        copy = UndirectedGraphNode(node.label)
        d[node] = copy
        que = [node]

        while que:
            cur = que.pop(0)
            neighbors = cur.neighbors
            for neighbor in neighbors:
                if neighbor not in d:
                    clone = UndirectedGraphNode(neighbor.label)
                    d[neighbor] = clone
                    que.append(neighbor)
                    d[cur].neighbors.append(clone)
                else:
                    d[cur].neighbors.append(d[neighbor])
        return copy