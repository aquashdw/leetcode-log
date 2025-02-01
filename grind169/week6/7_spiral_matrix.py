from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        deltas = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]
        dir_idx = 0

        rows = len(matrix)
        cols = len(matrix[0])
        items = cols * rows

        check_bounds = lambda y, x: -1 < y < rows and -1 < x < cols
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        result.append(matrix[0][0])
        visited[0][0] = True
        now = [0, 0]
        while len(result) < items:
            while not check_bounds(now[0] + deltas[dir_idx][0], now[1] + deltas[dir_idx][1]) \
                    or visited[now[0] + deltas[dir_idx][0]][now[1] + deltas[dir_idx][1]]:
                dir_idx = (dir_idx + 1) % 4

            for i in range(2):
                now[i] += deltas[dir_idx][i]

            visited[now[0]][now[1]] = True
            result.append(matrix[now[0]][now[1]])

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
