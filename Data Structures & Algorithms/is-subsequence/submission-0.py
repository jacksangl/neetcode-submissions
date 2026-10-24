class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) > len(t):
            return False
        

        p1 = 0

        for i in range(len(t)):
            if p1 >= len(s): return True
            if s[p1] == t[i]:
                p1 += 1
        
        
        
        return True if p1 >= len(s) else False