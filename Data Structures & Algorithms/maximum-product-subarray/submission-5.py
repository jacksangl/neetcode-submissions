class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMax, curMin = 1, 1
        res = nums[0]

        for num in nums:
            if num == 0:
                curMax = curMin = 1
            tmp = num * curMax
            curMax = max(tmp, curMin*num, num)
            curMin = min(tmp, curMin*num, num)
            res = max(curMax, res)
        
        return res