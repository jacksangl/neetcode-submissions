class Solution:
    def trap(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        res = 0

        max_l, max_r = [0] * (len(heights) + 2), [0] * (len(heights) + 2) 

        for i in range(len(heights)):
            max_l[i+1] = max(max_l[i], heights[i])
        for i in range(len(heights), 0, -1):
            max_r[i] = max(max_r[i+1], heights[i-1])

        for i, height in enumerate(heights):
            res += min(max_l[i+1], max_r[i+1]) - height
        return res