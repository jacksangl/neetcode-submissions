class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        if n == 2 or n == 3: return []

        COLS = set()
        DOWN_D, UP_D = set(), set()
        res = []
        def backtrack(i,j, sol):
            if i >= n: return
            if j in COLS or (i-j) in DOWN_D or (i+j) in UP_D: return
            
            DOWN_D.add(i-j)
            UP_D.add(i+j)
            COLS.add(j)
            sol[i] = "."*j + "Q" + "."*(n-j-1)
            if i == n-1:
                res.append(sol[:])
            for dj in range(n):
                backtrack(i+1, dj, sol)
            sol[i] = "."*n
            DOWN_D.remove(i-j)
            UP_D.remove(i+j)
            COLS.remove(j)
        
        sol = ["."*n]*n
        for j in range(n):
            backtrack(0,j,sol)
    
        return res