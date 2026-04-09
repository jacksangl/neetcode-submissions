class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        seen = {}
        
        for r in range(len(s)):
            # add most seen to set
            seen[s[r]] = seen.get(s[r], 0) + 1
            most = max(seen.values())

            while l < r and r - l - most >= k:
                seen[s[l]]-= 1
                l += 1 

            res = max(res, r-l + 1 )
        return res


