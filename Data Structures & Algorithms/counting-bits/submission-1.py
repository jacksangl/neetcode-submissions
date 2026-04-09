class Solution:
    def countBits(self, n: int) -> List[int]:

        if n < 1:
            return [0]
        dp = [0] * (n + 1)
        dp[0] = 0
        offset = 1
        res = dp.copy()
        for i in range(1, n+1):
            if offset * 2 == i:
                offset *= 2
            
            dp[i] = 1 + dp[i - offset]
        return dp