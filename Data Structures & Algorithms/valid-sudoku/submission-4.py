class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            has = {}
            has2 = {}
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in has:
                        return False
                    else:
                        has[board[i][j]] = True

                if board[j][i] != '.':
                    if board[j][i] in has2:
                        return False
                    else:
                        has2[board[j][i]] = True

        for i in range(3):
            for l in range(3):
                has = {}
                for j in range(3):
                    for k in range(3):
                        if board[(j + i*3)][(k + l*3)] != '.':
                            if board[(j + i*3)][(k + l*3)] in has:
                                return False
                            else:
                                has[board[(j + i*3)][(k + l*3)]] = True
        
        return True