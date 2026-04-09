class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for s in strs:
            chars = [0] * 26
            for char in s:
                chars[ord(char) - ord('a')] += 1 
            chars = tuple(chars)
            groups[chars].append(s)
        return list(groups.values())
            