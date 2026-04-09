class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        l, r = 0, len(nums)-1
        triplets = set()

        
        for i in range(len(nums)):
            goal = nums[i]
            l, r = 0, len(nums)-1
            while l < r:
                cur = nums[l] + nums[r]
                if cur + goal == 0 and l != i and r != i:
                    c = [nums[l], goal, nums[r]]
                    c.sort()
                    c = tuple(c)
                    if c not in triplets:
                        res.append([nums[l], goal, nums[r]])
                    triplets.add(tuple(sorted([nums[l], goal, nums[r]])))
                if cur + goal < 0:
                    l += 1
                else:
                    r -= 1

        return res
