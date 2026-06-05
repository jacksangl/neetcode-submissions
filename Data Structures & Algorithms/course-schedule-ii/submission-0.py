class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        reqs = {}
        seen = set()
        res = []
        for i in range(numCourses):
            reqs[i] = []

        for course, pre in prerequisites:
            reqs[course].append(pre)
        

        def dfs(course, visited):
            if course in visited: return False
            if course in seen: return True
            visited.add(course)
            for child in reqs[course]:
                if not dfs(child, visited): return False
            seen.add(course)
            res.append(course)
            visited.remove(course)
            return True
       
        for course in range(numCourses):
            if course not in seen and not dfs(course, visited = set()):
                return []
            
        return res

