class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        l, r = 0, length -1

        while l <= r:
            median = (l+r) // 2
            check = nums[median]
            if check < target:
                l = median + 1
            elif check > target:
                r = median - 1
            else:
                return median

    

        return -1 