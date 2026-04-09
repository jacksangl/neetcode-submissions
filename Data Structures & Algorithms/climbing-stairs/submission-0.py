class Solution:
    def climbStairs(self, n: int) -> int:
        # brute force now we need to dynamic program it
        if n == 0:
            return 1
        s = 0

        if n > 1:
            s += self.climbStairs(n-2)
        if n>0:
            s += self.climbStairs(n-1)

        return s