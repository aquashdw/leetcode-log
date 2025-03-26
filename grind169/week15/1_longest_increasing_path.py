from typing import List


class Solution:
    def __init__(self):
        self.matrix = None
        self.dp = None
        self.check_bounds = None
        self.deltas = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1),
        ]

    def dfs(self, y, x):
        if self.dp[y][x] > 0:
            return self.dp[y][x]

        local_max = 1
        for delta in self.deltas:
            next_y, next_x = y + delta[0], x + delta[1]
            if not self.check_bounds(next_y, next_x) or self.matrix[next_y][next_x] <= self.matrix[y][x]:
                continue
            local_max = max(local_max, 1 + self.dfs(next_y, next_x))

        self.dp[y][x] = local_max
        return self.dp[y][x]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        width, height = len(matrix[0]), len(matrix)
        self.matrix = matrix
        self.dp = [[-1 for _ in range(width)] for _ in range(height)]
        self.check_bounds = lambda y, x: 0 <= y < height and 0 <= x < width
        global_max = 1
        for i in range(height):
            for j in range(width):
                global_max = max(global_max, self.dfs(i, j))

        return global_max


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
    print(solution.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
