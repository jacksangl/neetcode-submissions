class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix)-1, len(matrix[0])-1
        
        correct_row = None
        t, b, l, r, = 0, m, 0, n


        while t <= b:
          
            middle = (t+b) // 2
            # if middle row < target and (middle = last row or the next row is bigger)
            if matrix[middle][0] == target: return True
            elif matrix[middle][0] < target and (middle == m or matrix[middle+1][0] > target):
                correct_row = matrix[middle] 
                break
            elif matrix[middle][0] > target:
                b = middle - 1
            else:
                t = middle+1
        if correct_row is None: return False

        while l <= r:
            middle = (l + r) // 2
            if correct_row[middle] == target: return True
            elif correct_row[middle] < target: l = middle + 1
            else: r = middle - 1

        return False
