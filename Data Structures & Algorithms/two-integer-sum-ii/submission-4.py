class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i in range(len(nums)):
            num = nums[i]
            cache[num] = i
        
        for i in range(len(nums)):
            num = nums[i]
            if target-num == num:
                continue
            if target-num in cache:
                return [i+1, cache[target-num]+1]
        