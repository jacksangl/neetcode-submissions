class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        cache = {}
        def topdown(string):
            if string in cache:
                return cache[string]
            if string == s:
                return True
            elif len(string) >= n or string != s[:len(string)]:
                return False
            for word in wordDict:
                cache[string+word] = topdown(string+word)
                if cache[string+word]:
                    return True
            return False

        return topdown("")
