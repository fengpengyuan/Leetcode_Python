import collections

__author__ = 'fengpeng'


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        courses = [0] * numCourses
        for prerequisite in prerequisites:
            courses[prerequisite[0]] += 1
        que = []
        for i in xrange(numCourses):
            if courses[i] == 0:
                que.append(i)
                res.append(i)

        while que:
            course = que.pop(0)
            for prerequisite in prerequisites:
                if course == prerequisite[1]:
                    courses[prerequisite[0]] -= 1
                    if courses[prerequisite[0]] == 0:
                        res.append(prerequisite[0])
                        que.append(prerequisite[0])
        return res if len(res) == numCourses else []

    def findOrder2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        dict = collections.defaultdict(list)
        for prerequisite in prerequisites:
            dict[prerequisite[0]].append(prerequisite[1])
        visited = [0] * numCourses

        for i in xrange(numCourses):
            if self.detectCycle(i, visited, dict, res):
                return []
        return res

    def detectCycle(self, i, visited, dict, res):
        if visited[i] == -1:
            return True
        if visited[i] == 1:
            return False
        visited[i] = -1
        for course in dict[i]:
            if self.detectCycle(course, visited, dict, res):
                return True
        visited[i] = 1
        res.append(i)
        return False


prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print Solution().findOrder(4, prerequisites)

print Solution().findOrder2(4, prerequisites)