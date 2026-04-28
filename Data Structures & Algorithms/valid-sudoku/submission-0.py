class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        col_set = set()
        for i in range(9):
            row_set.clear()
            col_set.clear()
            for j in range(9):
                if board[i][j] in row_set or board[j][i] in col_set:
                    return False
                else:
                    if board[i][j] != ".":
                        row_set.add(board[i][j]) 
                    if board[j][i] != ".":
                        col_set.add(board[j][i])

        cube_set = set()
        for i in range(1,4):   
            for j in range(1, 4):
                r = i * 3
                c = j * 3
                cube_set.clear()
                for a in range(1,4):
                    for b in range(1,4):
                        if board[r-a][c-b] in cube_set:
                            return False
                        else:
                            if board[r-a][c-b] != ".":
                                cube_set.add(board[r-a][c-b])

        return True