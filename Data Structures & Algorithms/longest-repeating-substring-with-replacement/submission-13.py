class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r = 0 , len(s)-1
        cur = {}
        res = 1

        for r in range(len(s)):
            cur[s[r]] = cur.get(s[r], 0) + 1
            com = max(cur.values())
            while r - l - com+1 > k:
                cur[s[l]] -= 1
                l += 1
            
            res = max(res, r - l+1)
            print(res)
        res = max(res, r - l+1)
        return res