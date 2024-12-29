from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)
        return points[:k]


if __name__ == '__main__':
    solution = Solution()
    print(solution.kClosest(points=[[1, 3], [-2, 2]], k=1))
