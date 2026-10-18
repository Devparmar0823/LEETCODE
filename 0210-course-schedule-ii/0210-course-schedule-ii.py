from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Step 1: Initialize adjacency list and indegree tracker
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        # Step 2: Build the graph
        # [course, prereq] means prereq -> course
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1
            
        # Step 3: Queue all courses with 0 prerequisites (no incoming edges)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        order = []
        
        # Step 4: Process the queue
        while queue:
            current_course = queue.popleft()
            order.append(current_course)
            
            # Decrease the indegree for all neighboring dependent courses
            for dependent_course in adj_list[current_course]:
                indegree[dependent_course] -= 1
                # If all prerequisites for this course are met, add it to the queue
                if indegree[dependent_course] == 0:
                    queue.append(dependent_course)
                    
        # Step 5: If the order contains all courses, return it; otherwise, a cycle exists
        return order if len(order) == numCourses else []
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        order = []
        while queue:
            current_course = queue.popleft()
            order.append(current_course)
            for dependent_course in adj_list[current_course]:
                indegree[dependent_course] -= 1
                if indegree[dependent_course] == 0:
                    queue.append(dependent_course)
        return order if len(order) == numCourses else []
