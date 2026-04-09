class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return nums[0]
        elif length < 3:
            return max(nums[0], nums[1])
        elif length < 4:
            return max((nums[0]+nums[2]), nums[1])

        dp = [0]*(length)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]

        for i in range(3, length):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        print(dp)
        return max(dp[length-1], dp[length-2])