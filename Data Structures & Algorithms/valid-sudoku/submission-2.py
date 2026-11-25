class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()                
            for j in range(9):                
                if (board[i][j] == "."):
                    continue
                elif (board[i][j] in seen):
                    return False
                seen.add(board[i][j])

        for i in range(9):
            seen = set()          
            for j in range(9):
                
                if (board[j][i] == "."):
                    continue
                elif (board[j][i] in seen):
                    return False
                seen.add(board[j][i])
        

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        num = board[i][j]
                        if num == ".":
                            continue
                        elif (num in seen):
                            return False
                        seen.add(num)

        return True



        