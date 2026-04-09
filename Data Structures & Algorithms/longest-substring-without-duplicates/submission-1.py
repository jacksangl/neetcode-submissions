class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0

        # dict to store
        mp = {}
        max_length = 0

        # just basically looping over
        while r<len(s):
            # if current letter not in the map
            if s[r] in mp and mp[s[r]] >= l:
                l = mp[s[r]] + 1
            length = r - l + 1
            mp[s[r]] = r
            max_length = max(length, max_length)
            r += 1

        return max_length