class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac, atl = set(), set()
        rows, cols = len(heights), len(heights[0])
        def ocean(i,j,visited,prev):
            if i < 0 or i >= rows or j < 0 or j >= cols or heights[i][j] < prev or (i,j) in visited:
                return
            
            visited.add((i,j))
            ocean(i-1,j,visited,heights[i][j])
            ocean(i+1,j,visited,heights[i][j])
            ocean(i,j-1,visited,heights[i][j])
            ocean(i,j+1,visited,heights[i][j])
            
        for i in range(rows):
            ocean(i, 0, pac, -float('inf'))
            ocean(i, cols-1, atl, -float('inf'))
        for j in range(cols):
            ocean(0, j,pac , -float('inf'))
            ocean(rows-1, j,atl , -float('inf'))
        
        res = []
        for i in range(rows):
            for j in range(cols):

                if (i, j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res
            