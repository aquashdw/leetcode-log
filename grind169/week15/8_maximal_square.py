from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        height = len(matrix)
        width = len(matrix[0])
        sums = [[0 for _ in range(width + 1)]]
        for row in matrix:
            sums.append([0] + [int(x) for x in row])

        for i in range(1, width):
            sums[0][i] += sums[0][i - 1]

        for i in range(1, height + 1):
            sums[i][0] += sums[i - 1][0]
            for j in range(1, width + 1):
                sums[i][j] += sums[i][j - 1] + sums[i - 1][j] - sums[i - 1][j - 1]

        min_square = 0
        for i in range(1, height + 1):
            if i + min_square > height:
                break
            for j in range(1, width + 1):
                if j + min_square > width:
                    break
                for n in range(min_square + 1, min(height, width) + 1):
                    dr = [i + n - 1, j + n - 1]
                    if dr[0] > height or dr[1] > width:
                        break
                    ones = sums[dr[0]][dr[1]]
                    ones += sums[i - 1][j - 1]
                    ones -= sums[dr[0]][j - 1] + sums[i - 1][dr[1]]
                    if ones != n ** 2:
                        break
                    min_square = n

        return min_square ** 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximalSquare([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]))
    print(solution.maximalSquare([["0"]]))
    print(solution.maximalSquare([
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"]
    ]))
    print(solution.maximalSquare([["0", "1"], ["1", "0"]]))
