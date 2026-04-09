class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}
        i = 0
        for num in nums:
            if m.get(num) is not None:
                return True
            m[num] = i
            i += 1
        
        return False