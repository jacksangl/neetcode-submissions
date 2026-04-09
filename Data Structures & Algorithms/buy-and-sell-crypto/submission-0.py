class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0

        # can have a pointer l that 
        # stays at the lowest price 
        # while the r pointer keeps moving
        # through and then a max sell price
        profit = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                s = prices[r] - prices[l]
                profit = max(s, profit)
            else:
                l = r
            r += 1


        
        
        return profit