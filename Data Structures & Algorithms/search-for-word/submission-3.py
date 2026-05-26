class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])

        def backtrack(cur, i, j, idx):
            if cur == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == "." or idx >= len(word):
                return False
            correct = False
            if board[i][j] == word[idx]:
                store = board[i][j]
                board[i][j] = "."
                correct = call(cur + 1, i, j, idx+1) 
                board[i][j] = store

            return correct

        def call(cur, i, j, idx):
            return backtrack(cur, i+1, j, idx) or backtrack(cur, i, j+1, idx) or backtrack(cur, i-1, j, idx) or backtrack(cur, i, j-1, idx)

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    store = board[i][j] 
                    board[i][j] = "."
                    if call(1, i, j, 1): return True
                    board[i][j] = store
        return False

        