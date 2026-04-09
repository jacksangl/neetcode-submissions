class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ''' brute force
        # anytime u see a one u loop through the entire 
        # grid so O(n^2) and keep track until the island ends
        # definition of island ending is none of its points
        # are connected to any land except the island itself
        # so technically if the whole grid was ones there would
          be one island 
          this is o(n^2 * O(n^2) so o(n^4))
        '''
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def dfs(grid, row, col):
            if row < 0 or col < 0 or len(grid) <= row or len(grid[0]) <= col:
                return
            if visited[row][col] == 1 or grid[row][col] == '0':
                return
           
            visited[row][col] = 1
            dfs(grid, row, col+1)
            dfs(grid, row+1, col)
            dfs(grid, row, col-1)
            dfs(grid, row-1, col)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    dfs(grid, i, j)
                    islands += 1
        return islands
                

                    