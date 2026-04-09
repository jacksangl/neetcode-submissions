class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l, r, = 0, len(s1)
        s1_key = {}
        check = {}
        # count chars in the key word
        # also note chars in the check word
        for i in range(len(s1)):
            char = s1[i]
            char_s2 = s2[i]
            s1_key[char] = s1_key.get(char, 0) + 1
            check[char_s2] = check.get(char_s2, 0) + 1
        if s1_key == check:
            return True
        print(s1_key)
        while r < len(s2):
            char_s2 = s2[r]
            check[char_s2] = check.get(char_s2, 0) + 1
            check[s2[l]] -= 1
            if check[s2[l]] == 0:
                del check[s2[l]]
            print(check)
            if s1_key == check:
                return True
            r += 1 
            l += 1
        return False