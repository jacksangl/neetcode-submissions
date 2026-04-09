class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        length = len(nums)
        def backtrack(i):
            if i >= length:
                res.append(sub.copy())
                return
            sub.append(nums[i])
            backtrack(i+1)
            sub.pop()
            backtrack(i+1)
        backtrack(0)
        return res
