import collections
import heapq

__author__ = 'fengpeng'


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets:
            return []
        res = []
        dict = {}
        for ticket in tickets:
            if ticket[0] in dict:
                heapq.heappush(dict[ticket[0]], ticket[1])
            else:
                q = []
                heapq.heappush(q, ticket[1])
                dict[ticket[0]] = q

        self.dfs("JFK", dict, res)
        return res

    def dfs(self, start, dict, res):
        if start not in dict:
            res.insert(0, start)
            return
        destinations = dict[start]

        while destinations:
            des = heapq.heappop(destinations)
            self.dfs(des, dict, res)
        res.insert(0, start)

    def findItinerary2(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        itinerary = []
        map = {}
        for ticket in tickets:
            if ticket[0] in map:
                heapq.heappush(map[ticket[0]], ticket[1])
            else:
                q = []
                heapq.heappush(q, ticket[1])
                map[ticket[0]] = q
        stk = ['JFK']

        while stk:
            top = stk[-1]
            if top in map and map[top]:
                stk.append(heapq.heappop(map[top]))
            else:
                itinerary.insert(0, top)
                stk.pop()
        return itinerary


tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
print Solution().findItinerary(tickets)
print Solution().findItinerary2(tickets)