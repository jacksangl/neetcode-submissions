class Solution:
    def climbStairs(self, n: int) -> int:
        paths = {}

        def dp(n: int):
            if n == 0:
                return 1
            if n in paths:
                return paths[n]
            if n > 1:
                paths[n] = dp(n-2) + dp(n-1)
            elif n > 0:
                paths[n] = dp(n-1)
            return paths[n]

        return dp(n)