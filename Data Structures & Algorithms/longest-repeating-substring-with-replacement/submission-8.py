class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        l = 0
        cache = {}
        most_common = ""
        for r, char in enumerate(s):
            cache[char] = cache.get(char, 0) + 1
            most_common = max(cache, key=cache.get)
            while r - l + 1 - cache[most_common] > k:
                if cache[s[l]] > 0:
                    cache[s[l]] -= 1
                else:
                    del cache[s[l]]
                l += 1
                most_common = max(cache, key=cache.get)
            print(s[l:r+1])
            res = max(res, r-l+1)
        return res
