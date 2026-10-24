class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}

        def topdown(idx, cur):
            if (idx, cur) in memo:
                return memo[(idx,cur)]
            key = (idx, cur)
            if idx >= len(s):
                return 0.5
            cur += int(s[idx])
            if cur == 0 or cur > 26:
                return 0
            # do recursion for next indx where u either add to cur or start
            # a new char
            
            memo[key] = topdown(idx+1, cur*10) + topdown(idx+1, 0)
            return memo[key]
        return int(topdown(0, 0))
