class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        reqs = {}
        seen = set()
        for i in range(numCourses):
            reqs[i] = []
        
        
        for course, prereq in prerequisites:
            reqs[prereq].append(course)
    



        def finish(cur, visited):
            if cur in visited: return False
            seen.add(cur)
            visited.add(cur)
            for course in reqs[cur]:
                if not finish(course, visited):
                    return False
            visited.remove(cur)

            return True
        
        for _, prereq in prerequisites:
            if prereq not in seen and not finish(prereq, visited = set()):
                return False
        return True
        



