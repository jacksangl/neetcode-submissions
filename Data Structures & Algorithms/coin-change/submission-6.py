class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins = sorted(coins, reverse=True)

        res = 1
        cache = {}

        def topdown(cur, idx):
            if (cur, idx) in cache:
                return cache[(cur,idx)]
            if cur == amount:
                return 0
            if cur > amount or idx == len(coins):
                return float('inf')
            
            cache[(cur,idx)] = min(
                1 + topdown(cur + coins[idx], idx),
                topdown(cur, idx + 1)
            )
            return cache[(cur,idx)]
        res = topdown(0,0)
        return res if res != float('inf') else -1



        