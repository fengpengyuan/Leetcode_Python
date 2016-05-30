import collections

__author__ = 'fengpeng'


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courses = [0] * numCourses
        for prerequisite in prerequisites:
            courses[prerequisite[0]] += 1

        que = []
        for i in xrange(numCourses):
            if courses[i] == 0:
                que.append(i)
        finishes = len(que)
        while que:
            course = que.pop(0)
            for prerequisite in prerequisites:
                if course == prerequisite[1]:
                    courses[prerequisite[0]] -= 1
                    if courses[prerequisite[0]] == 0:
                        finishes += 1
                        que.append(prerequisite[0])
        return finishes == numCourses


    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        d = collections.defaultdict(list)
        for prerequisite in prerequisites:
            d[prerequisite[0]].append(prerequisite[1])
        visited = [0] * numCourses
        for i in xrange(numCourses):
            if self.detectCycle(i, visited, d):
                return False
        return True

    def detectCycle(self, i, visited, d):
        if visited[i] == -1:
            return True
        if visited[i] == 1:
            return False
        visited[i] = -1
        for course in d[i]:
            if self.detectCycle(course, visited, d):
                return True
        visited[i] = 1
        return False


prerequisites = [[1, 0]]
print Solution().canFinish(2, prerequisites)