class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        m, n = len(grid), len(grid[0])
        INF = 2147483647
        visited = {}
        def dfs(i, j, cur):
            nonlocal INF
            nonlocal call
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == -1:
                return
            if ((i,j) in visited and visited[(i,j)] == call):
                if cur < grid[i][j]:
                    grid[i][j] = min(cur, grid[i][j])
                    visited[(i,j)] = call
                    dfs(i+1, j, cur+1)
                    dfs(i-1, j, cur+1)
                    dfs(i, j+1, cur+1)
                    dfs(i, j-1, cur+1)
                    
                return
            
            grid[i][j] = min(cur, grid[i][j])
            visited[(i,j)] = call
            dfs(i+1, j, cur+1)
            dfs(i-1, j, cur+1)
            dfs(i, j+1, cur+1)
            dfs(i, j-1, cur+1)
            
        call = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i,j, 0)
                    call += 1