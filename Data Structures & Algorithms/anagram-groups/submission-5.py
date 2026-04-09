class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        cache = defaultdict(list)

        for string in strs:
            check = [0] * 26
            for char in string:
                check[ord(char)-ord('a')] += 1
            key = tuple(check)
            cache[key].append(string)
        return list(cache.values())