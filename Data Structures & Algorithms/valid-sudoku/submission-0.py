
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        delimiter = "."
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        board_set = defaultdict(set)

        n = len(board)

        for row in range(0, n):
            for col in range(0, n):
                value = board[row][col]

                if value == delimiter:
                    continue

                board_box = (row//3, col//3) 

                if value in col_set[col] or value in row_set[row] or value in board_set[board_box]:
                    return False
                

                col_set[col].add(value)
                row_set[row].add(value)
                board_set[board_box].add(value)
        return True


        






                



        