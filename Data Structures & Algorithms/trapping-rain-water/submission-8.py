class Solution:
    def trap(self, heights: List[int]) -> int:
        

        n = len(heights)

        left, right = [0]* n, [0]*n
        left[0] = right[-1] = 0

        for i in range(1, n):
            j = -i - 1
            left[i] = max(left[i-1], heights[i-1])
            right[j] = max(right[j+1], heights[j+1])
        
        res = 0
        for i in range(n):
            res += max(0, min(left[i], right[i]) - heights[i])
        
        return res
