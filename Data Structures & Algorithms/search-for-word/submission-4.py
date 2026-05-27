class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        m, n = len(board), len(board[0])

        def backtrack(cur, i, j, idx):
            if cur == len(word): return True

            if (i >= m or i < 0 or j >= n or j < 0 or idx >= len(word) or
                board[i][j] == "." or board[i][j] != word[idx]):
                return False
            store = board[i][j]
            board[i][j] = "."
            res = call(cur+1, i, j, idx+1)
            board[i][j] = store
            return res

        def call(cur, i, j, idx):
            return (backtrack(cur, i+1, j, idx) or
            backtrack(cur, i, j+1, idx) or
            backtrack(cur, i-1, j, idx) or
            backtrack(cur, i, j-1, idx)) 

        for i in range(m):
            for j in range(n):
                if backtrack(0, i, j, 0): return True
        
        return False

            