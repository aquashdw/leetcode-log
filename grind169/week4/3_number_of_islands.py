from collections import deque
from typing import List


class Solution:
    deltas = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])

        def check_bounds(y, x):
            return -1 < y < height and -1 < x < width

        visited = [[False for _ in range(width)] for _ in range(height)]
        isles = 0

        for i in range(height):
            for j in range(width):
                if grid[i][j] == "0" or visited[i][j]:
                    visited[i][j] = True
                    continue
                isles += 1
                visited[i][j] = True
                start = (i, j)
                to_visit = deque()
                to_visit.append(start)
                while to_visit:
                    now = to_visit.popleft()
                    for delta in self.deltas:
                        next_y = now[0] + delta[0]
                        next_x = now[1] + delta[1]
                        if not check_bounds(next_y, next_x):
                            continue
                        if visited[next_y][next_x]:
                            continue
                        visited[next_y][next_x] = True
                        if grid[next_y][next_x] == "0":
                            continue
                        to_visit.append((next_y, next_x))

        return isles


if __name__ == '__main__':
    solution = Solution()
    print(solution.numIslands(
        [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
