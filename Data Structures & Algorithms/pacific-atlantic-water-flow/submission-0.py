class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # top left pacific right bottom atlantic
        # heights[r][c] is height above sea level
        # water can flow in all l r u d
        # from a cell with equal height or lower
        # return in a 2d list where each element is a coord
        height, length = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(prev, r, c, visit):
            if ((r,c) in visit or r < 0 or c > length - 1 
                or c < 0 or r > height - 1 or 
                heights[r][c] < prev):
                return
            visit.add((r, c))
            dfs(heights[r][c], r-1, c, visit)
            dfs(heights[r][c], r+1, c, visit)
            dfs(heights[r][c], r, c-1, visit)
            dfs(heights[r][c], r, c+1, visit)

        for c in range(length):
            dfs(heights[0][c], 0, c, pac)
            dfs(heights[height-1][c], height-1, c, atl)
        for r in range(height):
            dfs(heights[r][0], r, 0, pac)
            dfs(heights[r][length-1], r, length-1, atl)
        
       
        
        flow = list()
        for r in range(height):
            for c in range(length):
                if (r, c) in atl and (r, c) in pac:
                    flow.append([r,c])

        return flow
                