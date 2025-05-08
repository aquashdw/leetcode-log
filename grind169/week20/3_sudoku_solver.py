from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def check_row(row):
            used = set()
            for i in range(9):
                val = board[row][i]
                if val == ".":
                    continue
                if val in used:
                    return False
                used.add(val)
            return True

        def check_col(col):
            used = set()
            for i in range(9):
                val = board[i][col]
                if val == ".":
                    continue
                if val in used:
                    return False
                used.add(val)
            return True

        def check_box(y, x):
            used = set()
            lu_y, lu_x = y // 3 * 3, x // 3 * 3
            for i in range(3):
                for j in range(3):
                    val = board[lu_y + i][lu_x + j]
                    if val == ".":
                        continue
                    if val in used:
                        return False
                    used.add(val)
            return True

        fill_order = sorted([i for i in range(9)], key=lambda x: board[x].count("."))

        def dfs(y, x):
            if x == 9:
                y += 1
                x = 0
            if y == 9:
                return True
            row = fill_order[y]
            if board[row][x] != ".":
                return dfs(y, x + 1)

            for i in range(1, 10):
                board[row][x] = str(i)
                if not (check_row(row) and check_col(x) and check_box(row, x)):
                    continue
                if dfs(y, x + 1):
                    return True
            board[row][x] = "."
            return False

        dfs(0, 0)


if __name__ == '__main__':
    solution = Solution()
    board = [[".", ".", ".", ".", ".", ".", ".", ".", "."], [".", "9", ".", ".", "1", ".", ".", "3", "."],
             [".", ".", "6", ".", "2", ".", "7", ".", "."], [".", ".", ".", "3", ".", "4", ".", ".", "."],
             ["2", "1", ".", ".", ".", ".", ".", "9", "8"], [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", "2", "5", ".", "6", "4", ".", "."], [".", "8", ".", ".", ".", ".", ".", "1", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    for row in board:
        print(" ".join(row))
    print()
    solution.solveSudoku(board)
    for row in board:
        print(" ".join(row))
