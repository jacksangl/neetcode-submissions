class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        length = len(prices)
        profit = 0
        while r< length:
            if (prices[l] < prices[r]):
                cur = prices[r] - prices[l]
                profit = max(profit, cur)
            else:
                l = r
            r+= 1
        return profit
