class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res, sol = [], ""
        
        def backtrack(o, c):
            nonlocal sol
            if o + c == 2*n:
                res.append(sol)
                return
            
            if o < n:
                sol += "("
                backtrack(o+1, c)
                sol = sol[:-1]
            
            if o > c:
                sol += ")"
                backtrack(o, c+1)
                sol = sol[:-1]
        backtrack(0,0)
        return res