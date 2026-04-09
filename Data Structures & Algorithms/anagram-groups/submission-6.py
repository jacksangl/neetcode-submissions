class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}

        for string in strs: 
            counts = [0]*26
            string = string.lower()
            for letter in string:
                counts[ord(letter)-ord('a')] += 1
            key = tuple(counts)
            if key in cache:
                cache[key].append(string)
            else:
                cache[key] = [string]
        return list(cache.values())
