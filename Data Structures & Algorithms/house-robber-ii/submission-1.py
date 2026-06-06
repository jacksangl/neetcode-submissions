class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or n== 2: return max(nums)
        dp1 = [0] * n
        dp2 = [0] * n
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        dp2[-1] = nums[-1]
        dp2[-2] = max(nums[-1], nums[-2])

        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
        for i in range(n-3, 0, -1):
            dp2[i] = max(dp2[i+1], dp2[i+2] + nums[i])
        print(dp1)
        print(dp2)
        return max(dp2[1], dp1[-2])
        


        