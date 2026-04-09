class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        l, r = 0, len(nums) -1
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1 
        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                l = middle + 1
            elif nums[middle] < target:
                r = middle - 1
        
            
        return -1