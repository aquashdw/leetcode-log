from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []

        def check_queens(queens, row, new_queen):
            if new_queen in queens:
                return False

            for i in range(row):
                row_diff = row - i
                col_diff = abs(queens[i] - new_queen)
                if row_diff == col_diff:
                    return False
            return True

        def set_queens(queens):
            now = len(queens)
            if now == n:
                result = []
                for queen in queens:
                    result.append("".join(["Q" if i == queen else "." for i in range(n)]))
                results.append(result)
                return

            for i in range(n):
                if not check_queens(queens, now, i):
                    continue
                queens.append(i)
                set_queens(queens)
                queens.pop()

        set_queens([])

        return results


if __name__ == '__main__':
    solution = Solution()
    print((solution.solveNQueens(4)))
