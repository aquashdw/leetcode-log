from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(idx):
            visited = [False for _ in range(9)]
            for num_str in board[idx]:
                if num_str == '.':
                    continue
                num = ord(num_str) - ord('0') - 1
                if visited[num]:
                    return False
                visited[num] = True
            return True

        def check_col(idx):
            visited = [False for _ in range(9)]
            for row in range(9):
                num_str = board[row][idx]
                if num_str == '.':
                    continue
                num = ord(num_str) - ord('0') - 1
                if visited[num]:
                    return False
                visited[num] = True
            return True

        def check_square(idx):
            visited = [False for _ in range(9)]
            row_start = (idx // 3) * 3
            col_start = (idx % 3) * 3
            for i in range(3):
                for j in range(3):
                    row = row_start + i
                    col = col_start + j
                    num_str = board[row][col]
                    if num_str == '.':
                        continue
                    num = ord(num_str) - ord('0') - 1
                    if visited[num]:
                        return False
                    visited[num] = True
            return True

        for i in range(9):
            if not (check_row(i) and check_col(i) and check_square(i)):
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    print(solution.isValidSudoku(
        [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
