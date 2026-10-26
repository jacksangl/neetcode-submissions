class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # i + j + k = 0
        # j + k = -i
        res = []
        nums.sort()
        triples = set()

        for i, num in enumerate(nums):
            num = -num

            j, k = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                left, right = nums[j], nums[k]
                if left + right < num:
                    j += 1
                elif left + right > num:
                    k -= 1
                else:
                    if (nums[i],nums[j], nums[k]) not in triples:
                        res.append([nums[i],nums[j], nums[k]])
                    
                    triples.add((nums[i],nums[j], nums[k]))
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]: j += 1
                    while j < k and nums[k] == nums[k+1]:k-=1
        return res
