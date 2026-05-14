class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            has = {}
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in has:
                        print(board[i][j])
                        return False
                    else:
                        has[board[i][j]] = True

        for i in range(9):
            has = {}
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in has:
                        return False
                    else:
                        has[board[j][i]] = True

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