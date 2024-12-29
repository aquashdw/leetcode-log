from collections import deque
from typing import List


class Solution:
    """
    first try: double bfs
    deltas = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    height = -1
    width = -1

    def check_bounds(self, y, x):
        return -1 < y < self.height and -1 < x < self.width

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.width = len(mat[0])
        self.height = len(mat)
        width, height = self.width, self.height
        result = [[-1 for _ in range(width)] for _ in range(height)]
        queue_now = deque()
        queue_next = deque()
        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue_next.append((i, j))

        while len(queue_next) != 0:
            queue_now, queue_next = queue_next, queue_now
            while len(queue_now) != 0:
                now_y, now_x = queue_now.popleft()
                now_val = result[now_y][now_x]
                for delta in self.deltas:
                    next_y, next_x = now_y + delta[0], now_x + delta[1]
                    if not self.check_bounds(next_y, next_x) or result[next_y][next_x] != -1:
                        continue

                    result[next_y][next_x] = now_val + 1
                    queue_next.append((next_y, next_x))

        return result
    """

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        width, height = len(mat[0]), len(mat)
        for y in range(height):
            for x in range(width):
                if mat[y][x] > 0:
                    top_value = mat[y - 1][x] + 1 if y > 0 else 10000
                    left_value = mat[y][x - 1] + 1 if x > 0 else 10000
                    mat[y][x] = min(top_value, left_value)

        for rev_y in range(height):
            y = height - rev_y - 1
            for rev_x in range(width):
                x = width - rev_x - 1
                if mat[y][x] > 1:
                    bot_value = mat[y + 1][x] + 1 if y + 1 < height else 10000
                    right_value = mat[y][x + 1] + 1 if x + 1 < width else 10000
                    mat[y][x] = min(mat[y][x], bot_value, right_value)

        return mat


if __name__ == '__main__':
    solution = Solution()
    print(solution.updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(solution.updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1 for _ in range(3)]]))
