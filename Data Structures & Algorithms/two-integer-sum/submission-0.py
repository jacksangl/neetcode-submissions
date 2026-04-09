class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Sum = {}
        return_value = []
        find = 0

        for i, num in enumerate(nums):
            find = target - num
            if find in Sum and Sum[find] != i:
                return_value = [Sum[find], i]
                break
            Sum[num] = i



        return return_value



        """
            Obviously the brute force solution is a double for loop
            But this can be implemented using a hash map for constant 
            time lookup O(1)
        """