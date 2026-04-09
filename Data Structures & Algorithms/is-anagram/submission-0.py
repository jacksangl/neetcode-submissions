class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        n = {}
        if len(s) != len(t):
            return False

        for a, b in zip(s, t):
            m[a] = m.get(a, 0)+1
            n[b] = n.get(b, 0)+1

        for letter in s:
            if letter not in n:
                return False
            if m[letter] != n[letter]:
                return False

        return True


