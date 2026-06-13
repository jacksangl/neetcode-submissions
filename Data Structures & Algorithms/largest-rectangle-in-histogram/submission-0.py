class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        

        left, right = [], []
        n = len(heights)
        res = 0
        for i in range(n):

            lptr, rptr = i-1, i+1

            while lptr >= 0:
                if heights[lptr] >= heights[i]:
                    lptr -= 1
                else: break
            while rptr < n:
                if heights[rptr] >= heights[i]:
                    rptr += 1
                else:
                    break
            
            res = max(res, heights[i] * (rptr - lptr - 1))
        return res