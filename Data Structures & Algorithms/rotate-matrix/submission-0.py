class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])

        for j in range(n):
            t, b = 0, n-1
            while t < b:
                matrix[t][j], matrix[b][j] = matrix[b][j], matrix[t][j]
                t +=1 
                b -= 1
        for i in range(m):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
         