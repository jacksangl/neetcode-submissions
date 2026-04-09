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
        exclude_dp = [0] * len(nums)
        exclude_dp[0] = 0
        exclude_dp[1] = nums[1]
        exclude_dp[2] = nums[2]

        for i in range(3, len(nums)):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
            exclude_dp[i] = nums[i] + max(exclude_dp[i-2], exclude_dp[i-3])
        dp[length-1] -= nums[length-1]



        return max(dp[-1], dp[-2], exclude_dp[-1])