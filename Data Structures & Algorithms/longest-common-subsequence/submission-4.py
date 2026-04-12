from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        

        m = len(text1)
        n = len(text2)

        @cache
        def topdown(i, j):
            if i == m or j == n:
                return 0
            elif text1[i] == text2[j]:
                return topdown(i+1, j+1) + 1
            else:
                return max(topdown(i,j+1), topdown(i+1, j))
        
        return topdown(0,0)
            