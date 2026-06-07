class Solution:
    def trap(self, heights: List[int]) -> int:
        

        n = len(heights)
        left, right = heights[0], heights[-1]
        l, r = 0, n-1
        res = 0
        
        while l < r:
            if left < right:
                l += 1
                left = max(left, heights[l])
                res += left - heights[l]
            else:
                r -= 1
                right = max(right, heights[r])
                res += right - heights[r]

        
        return res