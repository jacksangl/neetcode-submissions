class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        dp = [(1,1)] * n
        dp[0] = (1, nums[0])
        for i in range(1, n):
            
            max_length = 0
            for j in range(0, i):

                if dp[j][1] < nums[i]:
                    max_length = max(dp[j][0], max_length)
            
            dp[i] = (max_length+1, nums[i])
            res = max(dp[i][0], res)
        return res
    