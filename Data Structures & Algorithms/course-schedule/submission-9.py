class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courses = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            courses[course].append(prereq)

        
        def solve(course, prev, visited):
            if course in visited:
                return False
            visited.add(course)
            for prereq in courses[course]:
                if not solve(prereq, course, visited):
                    return False
            visited.remove(course)
            return True
        
        
        for i in range(numCourses):
            if not solve(i, -1, set()):
                return False
            
        return True