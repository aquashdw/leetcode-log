class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            paths[0][i] = 1
        for i in range(m):
            paths[i][0] = 1

        for i in range(1, m):
            paths[i][0] = paths[i - 1][0]
            for j in range(1, n):
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

        return paths[m - 1][n - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(3, 7))
