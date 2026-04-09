class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ##
        ## brute force

        products = []
        for i in range(len(nums)):
            s = 1
            for j in range(len(nums)):
                if j != i:
                    s*= nums[j]
            products.append(s)
        
        return products