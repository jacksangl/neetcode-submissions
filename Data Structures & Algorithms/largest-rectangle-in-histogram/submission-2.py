class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stk = []
        n = len(heights)
        res = 0

        for i, height in enumerate(heights):
            start = i
            while stk and height <= stk[-1][0]:
                h, pos = stk.pop()
                width = i - pos
                res = max(res, width*h)
                start = pos
            stk.append((height, start))
        
        while stk:
            h, pos = stk.pop()
            width = n - pos
            res = max(res, width*h)
        return res