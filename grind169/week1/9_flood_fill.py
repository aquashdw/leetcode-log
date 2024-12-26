from typing import List
from collections import deque


class Solution:
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

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target = image[sr][sc]
        if target == color:
            return image

        self.height = len(image)
        self.width = len(image[0])

        image[sr][sc] = color
        visited = [[False for _ in range(self.width)] for _ in range(self.height)]
        visited[sr][sc] = True
        queue = deque()
        queue.append((sr, sc))
        while len(queue) != 0:
            now = queue.popleft()
            for delta in self.deltas:
                next_ = tuple(map(sum, zip(now, delta)))
                if not self.check_bounds(*next_) or visited[next_[0]][next_[1]] or image[next_[0]][next_[1]] != target:
                    continue
                visited[next_[0]][next_[1]] = True
                image[next_[0]][next_[1]] = color
                queue.append(next_)
        return image


if __name__ == '__main__':
    solution = Solution()
    print(solution.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2))
