class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        chars = {}
        l = 0
        max_count = 0
        # i need to store the most popular char
        #somehow. could use a variable
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            max_count = max(max_count, chars[s[r]])

            while l < len(s) and (r-l-max_count+1 > k):
                delete = s[l]
                chars[delete] -= 1
                l += 1

            res = max(res, r-l+1)
        
        return res