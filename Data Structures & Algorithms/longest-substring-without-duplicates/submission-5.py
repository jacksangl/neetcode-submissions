class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        cache = set()
        counter = 0

        l = 0

        for r in range(len(s)):
            char = s[r]
            while l < r and char in cache:
                cache.remove(s[l])
                l += 1
            cache.add(s[r])
            res = max(r-l+1, res)
        return res

            