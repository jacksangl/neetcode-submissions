class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 3 or n == 2: return []

        res, sol = [], [["."] * n for _ in range(n)]

        
        cols = set()
        posDiag = set()
        negDiag = set()


        def backtrack(row):
            if row == n:
                board = ["".join(r) for r in sol]  
                res.append(board)              
                return
            
            for col in range(n):
                if col not in cols and row+col not in posDiag and row-col not in negDiag:
                    sol[row][col] = "Q"
                    cols.add(col)
                    posDiag.add(row+col)
                    negDiag.add(row-col)
                    backtrack(row+1)
                    sol[row][col] = "."
                    cols.remove(col)
                    posDiag.remove(row+col)
                    negDiag.remove(row-col)
            

            

        backtrack(0)
        return res

            
