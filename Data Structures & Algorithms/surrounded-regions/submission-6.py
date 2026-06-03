class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        dirs = [[1,0],[-1,0],[0,-1],[0,1]]
        rows, cols = len(board), len(board[0])

        def dfs(i,j):
            if i < 0 or j < 0 or i == rows or j == cols: return
            if board[i][j] != "O": return
            board[i][j] = "T"
            for di, dj in dirs:
                dfs(di+i, dj+j)
            

        for i in range(rows):
            for j in range(cols):
                spot = board[i][j]
                if ((i == 0 or j == 0 or i == rows-1 or j == cols -1) 
                    and board[i][j] == "O"):
                    dfs(i,j)
    
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O": board[i][j] = "X"
                elif board[i][j] == "T": board[i][j] = "O"
        