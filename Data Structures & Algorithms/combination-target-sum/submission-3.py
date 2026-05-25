class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res, sol = [], []
        n = len(nums)
        def backtrack(idx, total):
            # BASE CASE we are above target backtrack
            # or idx out of bounds
            if idx >= n or total > target:
                return
            if target == total:
                res.append(sol[:])
                return
            
            backtrack(idx+1, total)

            sol.append(nums[idx])
            total += nums[idx]
            backtrack(idx, total)
            total -= nums[idx]
            sol.pop()
        
        backtrack(0, 0)
        return res
        

