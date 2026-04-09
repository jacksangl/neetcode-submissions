class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # given a string of uppercase letters and an int k
        # you can choose k characters inside the string and replace all 
        # other characters with those letters
        # after performing K replacements aswell 
        # return the length of the longest substring with only one distinct
        # char

        # brute force solution

        chars = {}
        l = 0
        m = 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            
            if 1 + r - l - max(chars.values()) > k: 
                chars[s[l]] -= 1
                l += 1
            m = max(m, r-l+1)
        return m
        