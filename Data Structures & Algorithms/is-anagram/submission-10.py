class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = s.lower()
        t = t.lower()
        s_vals = [0] * 26
        t_vals = [0] * 26

        for letter in s:
            s_vals[ord(letter) - ord('a')] += 1
        for letter in t:
            t_vals[ord(letter) - ord('a')] += 1
        
        return s_vals == t_vals
        
