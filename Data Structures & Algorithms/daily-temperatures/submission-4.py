class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        # brute force loop over and find them ez O(n^2)
        # temperatures = [30,38,30,36,35,40,28]
    

        for i, cur_temp in enumerate(temperatures):
            while len(stack) > 0 and cur_temp > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append((cur_temp, i))
        
        return res 