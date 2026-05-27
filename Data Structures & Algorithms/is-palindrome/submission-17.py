class Solution:
    def isPalindrome(self, s: str) -> bool:
            i, j = 0, len(s)-1
            s = s.lower()

            while i <= j:
                while i <= len(s)-1 and not s[i].isalnum() : i += 1
                while j >= 0 and not s[j].isalnum() : j -= 1
                if i > j: break
                if s[i] != s[j]: return False
                i += 1
                j -= 1

            return True
        