class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        n = len(nums)
        idx = 0
        jump = nums[0]
        count = 0
        while jump:
            next_jump = 0
            if jump + idx >= n-1:
                return True
            for i in range(idx+1,idx+1+jump):
                option = nums[i]
                if option > 0 and option+i >= next_jump+idx:
                    next_jump = option
                    idx = i 
            if next_jump + idx >= n-1:
                return True
            if next_jump == 0:
                return False
            jump = next_jump
        return False