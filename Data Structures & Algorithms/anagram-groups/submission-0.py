class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return [[""]]

        anagrams = {}

        for string in strs:
            key = [0] * 26
            for char in string:
                place = ord(char) - ord('a')
                key[place] += 1
            key = tuple(key)
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]

        return list(anagrams.values())