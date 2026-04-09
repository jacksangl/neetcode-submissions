class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # okay this is the original house 
        # robber sltn
        length = len(nums)
        if length < 2:
            return nums[0]
        if length < 3:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]

        for i in range(3, len(nums)):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
        
        return max(dp[-1], dp[-2])