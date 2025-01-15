from collections import deque
from typing import List


class Solution:
    deltas = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        to_visit = deque()
        next_visit = deque()

        def check_bounds(y, x):
            return -1 < y < height and -1 < x < width

        visited = [[False for _ in range(width)] for _ in range(height)]
        targets = 0
        for i in range(height):
            for j in range(width):
                visited[i][j] = True if grid[i][j] == 0 or grid[i][j] == 2 else False
                if grid[i][j] == 1:
                    targets += 1
                elif grid[i][j] == 2:
                    next_visit.append((i, j))

        days = 0
        if targets == 0:
            return days

        while targets > 0 and next_visit:
            to_visit, next_visit = next_visit, to_visit
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
                    targets -= 1
                    next_visit.append((next_y, next_x))
            days += 1

        if targets > 0:
            return -1

        return days


if __name__ == '__main__':
    solution = Solution()
    print(solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print(solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    print(solution.orangesRotting([[0, 2]]))
