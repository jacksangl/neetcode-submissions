class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set()
        for num in nums: num_set.add(num)
        starts = []
        for num in nums:
            if num -1 not in num_set: starts.append(num)
        res = 0
        for start in starts:
            cur = start
            while cur in num_set:
                cur += 1
            res = max(res, cur - start)
        return res