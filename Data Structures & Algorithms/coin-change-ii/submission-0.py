class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        m = len(coins)
        memo = {}
        
        def dfs(idx, cur):
            if (idx, cur) in memo:
                return memo[(idx,cur)]
            if cur > amount or idx >= m:
                return 0
            elif cur == amount:
                return 1

            memo[(idx, cur)] = dfs(idx, cur+coins[idx]) + dfs(idx+1, cur)
            return memo[(idx, cur)]
        return dfs(0,0)
