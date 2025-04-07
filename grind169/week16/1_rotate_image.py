from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            sub_n = n - 1 - i - i
            # lu = (i, i)
            # ru = (i, i + sub_n)
            # rd = (i + sub_n, i + sub_n)
            # ld = (i + sub_n, i)
            # print(lu, ru, rd, ld)
            for j in range(sub_n):
                # print((i, i + j), (i + j, i + sub_n), (i + sub_n, i + sub_n - j), (i + sub_n - j, i))
                # print((i + j, i + sub_n), (i + sub_n, i + sub_n - j), (i + sub_n - j, i), (i, i + j))
                matrix[i + j][i + sub_n], matrix[i + sub_n][i + sub_n - j], matrix[i + sub_n - j][i], matrix[i][i + j] = \
                    matrix[i][i + j], matrix[i + j][i + sub_n], matrix[i + sub_n][i + sub_n - j], matrix[i + sub_n - j][
                        i]
            # print()


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(matrix)
    for row in matrix:
        print(row)
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solution.rotate(matrix)
    for row in matrix:
        print(row)
