class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search on entire matrix
        n = len(matrix[0])
        m = len(matrix)
        l_row, r_row = 0, m-1

        #conditions run binary search through the row if the
        # middle row left and right pointers are < target and > target
        while l_row <= r_row:
            middle_row = (l_row + r_row) // 2
            l, r = 0, n-1
            if matrix[middle_row][r] < target: 
                l_row = middle_row + 1
            elif matrix[middle_row][l] > target:
                r_row = middle_row - 1
            else:
                while l <= r:
                    middle = (r+l) // 2
                    if matrix[middle_row][middle] > target:
                        r = middle - 1
                    elif matrix[middle_row][middle] < target:
                        l = middle + 1
                    else:
                        return True
                break
            


        return False


        