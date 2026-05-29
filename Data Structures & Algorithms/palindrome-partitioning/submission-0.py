class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []
        def palindrome(s):
            return s == s[::-1]
        def backtrack(start):
            if start >= len(s):
                res.append(sol[:])
                return
            for i in range(start, len(s)):
                string = s[start:i+1]
                if palindrome(string): 
                    sol.append(string)
                    backtrack(i+1)

                    sol.pop()
        backtrack(0)
        return res

            
            

