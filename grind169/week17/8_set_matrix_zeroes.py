from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        for i in range(cols):
            if matrix[0][i] == 0:
                first_row_zero = True
                break

        first_col_zero = False
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, cols):
            if matrix[0][i] == 0:
                for j in range(1, rows):
                    matrix[j][i] = 0

        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0

        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
        if first_row_zero:
            for i in range(cols):
                matrix[0][i] = 0


if __name__ == '__main__':
    solution = Solution()
    # matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    # solution.setZeroes(matrix)
    # print(matrix)
    # matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    # solution.setZeroes(matrix)
    # print(matrix)
    matrix = [[1, 0]]
    solution.setZeroes(matrix)
    print(matrix)
