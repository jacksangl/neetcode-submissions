class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # Find the last row whose first value <= target
        l, r = 0, m - 1

        while l <= r:
            middle = (l + r) // 2

            if matrix[middle][0] == target:
                return True
            elif matrix[middle][0] < target:
                l = middle + 1
            else:
                r = middle - 1

        row = r
        if row < 0:
            return False

        # Search within that row
        l, r = 0, n - 1

        while l <= r:
            middle = (l + r) // 2

            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                l = middle + 1
            else:
                r = middle - 1

        return False