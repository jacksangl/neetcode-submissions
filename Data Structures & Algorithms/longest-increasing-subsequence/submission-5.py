from functools import cache
class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        
        

        @cache
        def topdown(idx, last):
            if idx >= len(nums):
                return 0
            
            if nums[idx] > last:
                return max(
                    topdown(idx+1, nums[idx]) + 1, 
                    topdown(idx+1, last)
                )
            else:
                return topdown(idx+1, last)
        return topdown(0, -1001)