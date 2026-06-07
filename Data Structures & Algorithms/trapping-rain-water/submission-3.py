class Solution:
    def trap(self, heights: List[int]) -> int:
        

        n = len(heights)
        left, right = [0]* n, [0] * n
        left[0] = 0
        right[-1] = 0
        for i in range(1, n):
            left[i] = max(left[i-1], heights[i-1])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], heights[i+1])
        res = 0
        for i in range(n):
            res += min(left[i], right[i]) - heights[i] if min(left[i], right[i]) - heights[i] > 0 else 0 
        return res