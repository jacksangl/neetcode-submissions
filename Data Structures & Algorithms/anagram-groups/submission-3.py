class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict()
        for word in strs:
            check = [0] * 26
            for char in word:
                check[ord(char) - ord('a')] += 1
            key = tuple(check)
            if key in res:
                res[key].append(word)
            else:
                res[key] = [word]
        
        return list(res.values())