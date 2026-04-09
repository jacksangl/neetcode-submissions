class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cache = set()
        res = 1
        for num in nums:
            cache.add(num)

        for num in nums:
            if num-1 not in cache:
                cur = num

                while cur in cache:
                    res = max(res, cur-num+1)
                    cur += 1
        return res