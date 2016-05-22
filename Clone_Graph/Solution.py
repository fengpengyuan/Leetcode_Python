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
            return None
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
                #     d[cur].neighbors.append(clone)
                # else:
                #     d[cur].neighbors.append(d[neighbor])
                d[cur].neighbors.append(d[neighbor])
        return copy


    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        dict = {}
        copy = UndirectedGraphNode(node.label)
        dict[node] = copy
        self.dfs(node, dict)
        return copy

    def dfs(self, node, dict):
        if not node:
            return
        neighbors = node.neighbors
        for neighbor in neighbors:
            if neighbor not in dict:
                clone = UndirectedGraphNode(neighbor.label)
                dict[neighbor] = clone
                dict[node].neighbors.append(clone)
                self.dfs(neighbor, dict)
            else:
                dict[node].neighbors.append(dict[neighbor])

    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        dict = {}
        return self.clone(node, dict)

    def clone(self, node, dict):
        if not node:
            return None
        if node in dict:
            return dict[node]
        copy = UndirectedGraphNode(node.label)
        dict[node] = copy
        neighbors = node.neighbors
        for neighbor in neighbors:
            copy.neighbors.append(self.clone(neighbor, dict))
        return copy

    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        stk=[]
        visited={}
        copy =UndirectedGraphNode(node.label)
        stk.append(node)
        visited[node]=copy

        while stk:
            top = stk.pop()

            for neighbor in top.neighbors:
                if neighbor not in visited:
                    stk.append(neighbor)
                    visited[neighbor]=UndirectedGraphNode(neighbor.label)
                visited[top].neighbors.append(visited[neighbor])

        return copy

