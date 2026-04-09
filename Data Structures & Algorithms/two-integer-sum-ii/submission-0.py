class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}


        for i, num in enumerate(numbers):
            val = target - num
            if val in m and m[val] < i+1:
                return [m[val], i+1]
            m[num] = i+1
        
        return []
