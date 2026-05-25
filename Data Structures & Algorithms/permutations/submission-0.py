class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        res, sol = [], []
        n = len(nums)
        seen = set()
        def backtrack():

            if len(sol) == n:
                res.append(sol[:])
                return
            
            for i in range(n):
                if nums[i] in seen: continue
                sol.append(nums[i])
                seen.add(nums[i])
                backtrack()
                sol.pop()
                seen.remove(nums[i])
        backtrack()
        return res

