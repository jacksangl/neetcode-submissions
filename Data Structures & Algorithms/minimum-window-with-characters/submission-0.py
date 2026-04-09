class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        check = {}
        for char in t:
            check[char] = check.get(char, 0) + 1
        
        counts = {}
        l = 0
        res = "00" * 1000
        formed = 0  # add this line

        for r in range(len(s)):
            if s[r] in check:
                counts[s[r]] = counts.get(s[r], 0) + 1
                if counts[s[r]] == check[s[r]]:
                    formed += 1  # add this line

            while formed == len(check):  # replace old check==counts
                correct = s[l:r+1]
                if len(correct) < len(res):
                    res = correct

                if s[l] in check:
                    counts[s[l]] -= 1
                    if counts[s[l]] < check[s[l]]:
                        formed -= 1
                l += 1

        return "" if res == "00" * 1000 else res
