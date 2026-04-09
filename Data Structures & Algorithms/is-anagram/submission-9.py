class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cache_s = {}
        cache_t = {}

        for i in range(len(s)):
            cache_s[s[i]] = cache_s.get(s[i], 0) + 1
            cache_t[t[i]] = cache_t.get(t[i], 0) + 1
        return cache_s == cache_t