class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        
        m,n = len(grid), len(grid[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        def fine(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            return True

        INF = 2147483647
        visited = set()
        count = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                cords = queue.popleft()
                i, j = cords
                if not fine(i,j) or (i,j) in visited or grid[i][j] == -1 : continue

                visited.add((i,j))
                print(grid[i][j])
                grid[i][j] = count
                print(grid[i][j])
                queue.append((i - 1, j))
                queue.append((i + 1, j))
                queue.append((i, j - 1))
                queue.append((i, j + 1))

            count += 1


                