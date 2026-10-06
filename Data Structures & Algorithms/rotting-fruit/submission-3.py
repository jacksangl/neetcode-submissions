class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        res = 0

        starts = []
        m, n = len(grid), len(grid[0])
        nodes = set()

        seen = {}

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    starts.append((i,j))
                if grid[i][j] > 0:
                    nodes.add((i,j))
        if not starts and not nodes:
            return 0
        elif not starts:
            return -1


        def bfs(i, j, minute):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0: return
            
            if (i,j) in seen and seen[(i,j)] <= minute: return

            seen[(i,j)] = minute

            bfs(i+1, j, minute+1)
            bfs(i-1, j, minute+1)
            bfs(i, j+1, minute+1)
            bfs(i, j-1, minute+1)
        
        for i,j in starts:
            bfs(i,j, 0)
        
        # seen {(0,0): 1, ()}
        if len(seen) != len(nodes):
            return -1

        return max(seen.values())
