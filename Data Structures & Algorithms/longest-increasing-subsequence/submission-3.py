class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        dp = [1] * n
        for i in range(1, n):
            
            max_length = 0
            for j in range(0, i):

                if nums[j] < nums[i]:
                    max_length = max(dp[j], max_length)
            
            dp[i] = max_length + 1
            res = max(dp[i], res)
        return res
    