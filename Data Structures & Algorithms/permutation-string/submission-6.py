from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        check = {}
        cache = {}
        for i in range(len(s1)):
            check[s1[i]] = check.get(s1[i], 0) + 1
            cache[s2[i]] = cache.get(s2[i],0) + 1
        if cache == check:
            return True
        for r in range(len(s1), len(s2)):
            cache[s2[r]] = cache.get(s2[r],0) + 1
            if cache[s2[l]] == 1: del cache[s2[l]]
            else: cache[s2[l]] -= 1

            if check == cache:
                return True
            l += 1
        return check == cache
