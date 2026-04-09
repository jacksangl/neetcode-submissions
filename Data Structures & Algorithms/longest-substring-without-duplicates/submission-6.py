class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        cache = set()
        l = 0

        for r in range(len(s)):
            while l < r and s[r] in cache:
                cache.remove(s[l])
                l += 1
            cache.add(s[r])
            res = max(r-l+1, res)
        return res

            