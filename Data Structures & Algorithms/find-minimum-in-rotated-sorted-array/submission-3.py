class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        low = 1001

       

        while l < r:
            middle = (l+r) // 2
            low = min(low, nums[middle])

            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle

        return nums[l]