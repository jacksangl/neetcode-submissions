class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        length = len(nums)
        sub = []
        def backtrack(i, cur):
            if cur == target:
                res.append(sub.copy())
                return
            if i >= length or cur >= target:
                return
            sub.append(nums[i])
            backtrack(i, cur + nums[i])
            sub.pop()
            backtrack(i+1, cur)
            
        backtrack(0,0)

        return res