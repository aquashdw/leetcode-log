from collections import deque
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [
            [] for _ in range(n)
        ]
        for flight in flights:
            adj_list[flight[0]].append((flight[1], flight[2]))

        to_visit = deque()
        to_visit.append((src, 0, 0))
        dists = [float('inf') for _ in range(n)]
        dists[src] = 0

        while to_visit:
            now = to_visit.popleft()
            if now[1] > k:
                continue
            for flight in adj_list[now[0]]:
                next_, cost = flight
                if dists[next_] > now[2] + cost:
                    dists[next_] = now[2] + cost
                    to_visit.append((next_, now[1] + 1, dists[next_]))

        return -1 if dists[dst] == float('inf') else dists[dst]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))
    print(solution.findCheapestPrice(
        5,
        [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]],
        2,
        1,
        1,
    ))
