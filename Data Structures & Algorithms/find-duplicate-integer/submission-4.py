class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # naive

        nums.sort()
        prev = -1
        for num in nums:
            if num == prev:
                return num
            prev = num