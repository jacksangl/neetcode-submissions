class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        n = {}
        if len(s) != len(t):
            return False

        for a, b in zip(s, t):
            m[a] = m.get(a, 0)+1
            n[b] = n.get(b, 0)+1

        return m == n


