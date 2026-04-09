class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        cache = {}

        for string in strs:
            check = [0] * 26
            for char in string:
                check[ord(char)-ord('a')] += 1
            key = tuple(check)
            if key in cache:
                cache[key].append(string)
            else:
                cache[key] = [string]
        return list(cache.values())