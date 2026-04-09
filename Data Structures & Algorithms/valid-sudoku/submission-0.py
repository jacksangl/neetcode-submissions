class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        collums = defaultdict(set)
        grids = defaultdict(set)
    

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                if (value in rows[i]
                    or value in collums[j]
                    or value in grids[(i//3),j//3]):
                    return False
                rows[i].add(value)
                collums[j].add(value)
                grids[(i//3, j//3)].add(value)



        return True