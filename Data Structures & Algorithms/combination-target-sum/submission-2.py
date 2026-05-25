class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res, sol = [], []
        cur = 0
        n = len(nums)
        def backtrack(idx):
            # BASE CASE we are above target backtrack
            # or idx out of bounds
            nonlocal cur
            if idx >= n or cur > target:
                return
            if target == cur:
                res.append(sol[:])
                return
            
            backtrack(idx+1)

            sol.append(nums[idx])
            cur += nums[idx]
            backtrack(idx)
            cur -= nums[idx]
            sol.pop()
        
        backtrack(0)
        return res
        

