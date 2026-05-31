class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        p, a = set(), set()
        m, n = len(heights), len(heights[0])
        def dfs(i, j, visit, prev):
            if i >= m or j < 0 or i < 0 or j >= n  or (i,j) in visit or heights[i][j] < prev:
                return
            visit.add((i,j))
            dfs(i-1, j,visit, heights[i][j])
            dfs(i+1, j,visit, heights[i][j])
            dfs(i, j+1,visit, heights[i][j])
            dfs(i, j-1,visit, heights[i][j])
        
        for j in range(len(heights[0])):
            dfs(0, j, p, -float('inf'))
            dfs(len(heights)-1,j, a, -float('inf'))
        for i in range(len(heights)):
            dfs(i, 0,p, -float('inf'))
            dfs(i ,len(heights[0])-1,a, -float('inf'))
        
        res = []
        for r in range(m):
            for c in range(n):
                if (r, c) in p and (r, c) in a:
                    res.append([r, c])
        return res






