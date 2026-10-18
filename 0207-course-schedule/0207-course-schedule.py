from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        processed_courses = 0
        while queue:
            current_course = queue.popleft()
            processed_courses += 1
            for dependent_course in adj_list[current_course]:
                indegree[dependent_course] -= 1
                if indegree[dependent_course] == 0:
                    queue.append(dependent_course)
        return processed_courses == numCourses
