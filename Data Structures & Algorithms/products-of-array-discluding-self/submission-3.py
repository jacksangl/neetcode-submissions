class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1

        for num in nums:
            prefix *= num
            res.append(prefix)
        
        suffix = 1

        for i in range(len(nums)-1, 0, -1):
            res[i] =  res[i-1] * suffix
            suffix *= nums[i]
        
        res[0] = suffix 
        return res



        