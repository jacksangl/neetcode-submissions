class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) -1
        s = s.lower()

        while i < j:
            while s[i].isalnum() is False and i < j:
                i += 1
            while s[j].isalnum() is False and  i < j:
               j -= 1

            if (s[i] != s[j]): return False
            j -= 1
            i += 1

        return True
