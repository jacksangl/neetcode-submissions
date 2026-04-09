class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0,len(heights)-1
        area = 0
        i = 0
        while l<= r:
            area = max((min(heights[l], heights[r])) * (r-l), area)
            if heights[l] < heights[r]: l += 1
            else: r -= 1
        
        return area