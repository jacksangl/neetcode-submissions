class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        #O(2n)
        
        res, sol = [], []
        nums.sort()
        n = len(nums)
        def backtrack(idx, total):
            
            # we have a solution
            if total == target:
                res.append(sol[:])
                return
            if idx >= n or total > target:
                return
            sol.append(nums[idx])
            backtrack(idx+1, total + nums[idx])

            sol.pop()
            while idx < n-1 and nums[idx+1] == nums[idx]: 
                idx += 1
            backtrack(idx+1, total)

        
        backtrack(0,0)
        return res