from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        def check_bounds(y, x):
            return 0 <= y < m and 0 <= x < n

        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]

        deltas = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1),
        ]

        queue = deque()
        queue.append([0, 0])
        p_visited[0][0] = True
        for i in range(1, m):
            queue.append([i, 0])
            p_visited[i][0] = True
        for i in range(1, n):
            queue.append([0, i])
            p_visited[0][i] = True

        while queue:
            now = queue.popleft()
            for delta in deltas:
                next_y = now[0] + delta[0]
                next_x = now[1] + delta[1]
                if (check_bounds(next_y, next_x)
                        and not p_visited[next_y][next_x]
                        and heights[next_y][next_x] >= heights[now[0]][now[1]]):
                    p_visited[next_y][next_x] = True
                    queue.append([next_y, next_x])

        result = []
        queue.append([m - 1, n - 1])
        a_visited[m - 1][n - 1] = True
        if p_visited[m - 1][n - 1]:
            result.append(queue[-1])
        for i in range(m - 1):
            queue.append([i, n - 1])
            a_visited[i][n - 1] = True
            if p_visited[i][n - 1]:
                result.append(queue[-1])
        for i in range(n - 1):
            queue.append([m - 1, i])
            a_visited[m - 1][i] = True
            if p_visited[m - 1][i]:
                result.append(queue[-1])

        while queue:
            now = queue.popleft()
            for delta in deltas:
                next_y = now[0] + delta[0]
                next_x = now[1] + delta[1]
                if (check_bounds(next_y, next_x)
                        and not a_visited[next_y][next_x]
                        and heights[next_y][next_x] >= heights[now[0]][now[1]]):
                    a_visited[next_y][next_x] = True
                    if p_visited[next_y][next_x]:
                        result.append([next_y, next_x])
                    queue.append([next_y, next_x])
        return result


if __name__ == '__main__':
    solution = Solution()
    # print(
    #     solution.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
    print(solution.pacificAtlantic([[1, 2], [4, 3]]))
