class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        seen = set()

        # ROWS
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)
            seen.clear()

        # COLUMNS
        for col in range(9):
            for row in range(9):
                val = board[row][col]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)
            seen.clear()

        # BOXES
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val != ".":
                            if val in seen:
                                return False
                            seen.add(val)

        return True
