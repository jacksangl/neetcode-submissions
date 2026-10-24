from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        coins = sorted(coins, reverse=True)
        dp = [float('inf')] * (amount+1)
        
        for coin in coins:
            if coin > amount:
                continue
            dp[coin] = 1

        for current_amount in range(1, amount+1):
            for coin in coins:
                if coin <= current_amount:
                    remaining = current_amount - coin
                    dp[current_amount] = min(dp[remaining] + 1, dp[current_amount])
        
        return dp[-1] if dp[-1] != float('inf') else -1
        
