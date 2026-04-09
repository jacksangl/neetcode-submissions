class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        c = defaultdict(set)
        r = defaultdict(set)
        s = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                elif (val in c[j] or 
                      val in r[i] or 
                      val in s[(i//3, j//3)]):
                      return False
                c[j].add(val)
                r[i].add(val)
                s[(i//3, j//3)].add(val)
        return True
