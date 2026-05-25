class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res, sol = [], []
        n = len(nums)
        def backtrack(idx):
            if idx >= n:
                res.append(sol[:])
                return
            
            sol.append(nums[idx])
            backtrack(idx+1)
            sol.pop()

            while idx < n -1 and nums[idx+1] == nums[idx]:
                idx += 1
            
            backtrack(idx+1)
        
        backtrack(0)
        return res