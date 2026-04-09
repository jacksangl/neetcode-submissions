class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
            
        key = [0] * 26
        check = [0] * 26

        for r in range(len(s1)):
            key[ord(s1[r]) - ord('a')] += 1
            check[ord(s2[r]) - ord('a')] += 1

        if key == check:
            return True

        l, r = 0, len(s1)

        while r < len2:
            print(check)
            check[ord(s2[l]) - ord('a')] -= 1
            l += 1
            check[ord(s2[r]) - ord('a')] += 1
            if key == check:
                return True
            r += 1
        
        return False

