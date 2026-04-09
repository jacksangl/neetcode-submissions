class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        seen = set()

        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                elif (nums[i], nums[j], nums[k]) not in seen:
                    seen.add((nums[i], nums[j], nums[k]))
                    j += 1
                else: 
                    j += 1
    
        return list(seen)