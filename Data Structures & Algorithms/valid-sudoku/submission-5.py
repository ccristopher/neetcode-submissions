class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            r_list = []
            for c in r:
                if c != ".":
                    r_list.append(c)
            r_set = set(r_list)
            if len(r_set) != len(r_list):
                return False
        
        for col in range(len(board)):
            col_list = []
            for r in board:
                if r[col] != ".":
                    col_list.append(r[col])
            col_set = set(col_list)
            if len(col_set) != len(col_list):
                return False
        
        for r_box in range(len(board) // 3):
            for c_box in range(len(board) // 3):
                box_list = []
                for row in range(len(board) // 3):
                    for col in range(len(board) // 3):
                        if board[row + (r_box * (len(board) // 3))][col + (c_box * (len(board) // 3))] != ".":
                            box_list.append(board[row + (r_box * (len(board) // 3))][col + (c_box * (len(board) // 3))])
                box_set = set(box_list)
                if len(box_set) != len(box_list):
                    return False
        
        return True