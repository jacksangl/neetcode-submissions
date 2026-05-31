class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:



        res = 0

        queue = deque()
        rot = 2
        m, n = len(grid), len(grid[0])
        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == rot:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        visited = set()

        def fine(i,j):
            if ((i,j) in visited or i < 0 
                or i >= m or j < 0 or j >= n
                or grid[i][j] == 0):
                return False
            return True
        time = 0
        while queue:
            length = len(queue)

            for _ in range(length):
                i,j = queue.popleft()
                if not fine(i,j): continue

                visited.add((i,j))
                if grid[i][j] == 1:
                    fresh_count -= 1
                    res = time
                grid[i][j] = 2
                queue.append((i+1,j))
                queue.append((i-1,j))
                queue.append((i,j+1))
                queue.append((i,j-1))
            time += 1
        if fresh_count > 0:
            return -1
        
        return res
