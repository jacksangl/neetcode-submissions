class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            left, right = s[l], s[r]
            while  l < r and not left.isalnum():
                l += 1
                left = s[l]
            while l < r and not right.isalnum():
                r -= 1
                right = s[r]
            if left.lower() != right.lower():
                return False
            r -= 1
            l += 1
        return True