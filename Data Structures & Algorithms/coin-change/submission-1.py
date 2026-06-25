class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        dp[0] = 0
        n = len(coins)
        coins.sort()
        res = float('inf')
        for i in range(1, amount+1):
            for j in range(n):
                cur = i - coins[j]
                if cur < 0:
                    break
                elif cur == 0:
                    dp[i] = 1
                    break
                elif dp[cur] == -1:
                    continue
                else:
                    if dp[i] == -1:
                        dp[i] = 1 + dp[cur]
                    else:
                        dp[i] = min(dp[i], 1 + dp[cur])
        print(dp)
        return dp[amount]
                    