class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        i = 0
        j = 0
        res = 0
        while i < len(nums):
            num = nums[i]
            if num in numSet and num-1 not in numSet:
                count = 0
                while i < len(nums) and num in numSet:
                    count += 1
                    res = max(res, count)
                   
                    num += 1
            i += 1
        return res
