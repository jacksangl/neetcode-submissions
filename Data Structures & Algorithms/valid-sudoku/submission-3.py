class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # this iterates per row 
        cols = {}
        rows = {}
        for i in range(0, len(board), 3):
            # then per row iterates per board
            for j in range(0, len(board[0]), 3):
                
                # per row in the suoduko
                seen = set()
                for r in range(i, i+3):
                    # per col in the suoduko 
                    for c in range(j, j+3):
                        if board[r][c] == ".":
                            continue
                        if c not in cols:
                            cols[c] = {}
                        if r not in rows:
                            rows[r] = {}
                        if board[r][c] in seen or board[r][c] in cols[c] or board[r][c] in rows[r]:
                            print(board[r][c])
                            print(seen)
                            print(cols)
                            print(rows)
                            return False
                        seen.add(board[r][c])

                        rows[r][board[r][c]] = 1
                        cols[c][board[r][c]] = 1
        return True
                        
