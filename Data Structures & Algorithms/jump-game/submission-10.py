class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = nums[0]
        idx = 0
        
        while True:
            if idx == len(nums)-1:
                return True
            if nums[idx] > cur:
                cur = nums[idx]
            if cur == 0:
                return False
            cur -= 1
            idx += 1

        return True
