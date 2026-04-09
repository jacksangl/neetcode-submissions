class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf')
        res = 0
        for num in prices:
            if num < minimum:
                minimum = num
            else:
                res = max(res, num - minimum)
                print(num-minimum)

        return res
                