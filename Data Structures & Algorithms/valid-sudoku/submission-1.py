class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        # check boxes
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                for i in range(x, x + 3):
                    for j in range(y, y + 3):
                        value = board[i][j]

                        if value == ".":
                            continue
                        if value in seen:
                            return False
                        seen.add(value)
                seen.clear()

        # check rows
        for row in board:
            for num in row:
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
            seen.clear()

        # checks columns
        for col in range(len(board)):
            for row in range(len(board)):
                value = board[row][col]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
            seen.clear()

        return True