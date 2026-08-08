class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        startPoints = [(0,0), (3,0), (6,0),
                       (0,3), (3,3), (6,3),
                       (0,6), (3,6), (6,6)]

        seen = set()

        # check boxes
        for x, y in startPoints:
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    value = board[i][j]

                    if value == ".":
                        continue
                    if value in seen:
                        return False
                    seen.add(board[i][j])
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


