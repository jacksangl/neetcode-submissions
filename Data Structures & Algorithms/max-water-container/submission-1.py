class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            minHeight = min(heights[l], heights[r])
            water = (r-l) * minHeight
            print(water)
            res = max(res, water)
            if heights[l] == minHeight:
                l += 1
            else:
                r -= 1
        return res
