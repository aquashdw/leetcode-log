from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        min_bus = [float('inf') for _ in range(max(max(route) for route in routes) + 1)]
        if len(min_bus) - 1 < target or len(min_bus) - 1 < source:
            return -1

        min_bus[source] = 0

        flag = True
        while flag:
            flag = False
            for route in routes:
                dist = float('inf')
                for stop in route:
                    dist = min(dist, min_bus[stop])
                dist += 1
                for stop in route:
                    if min_bus[stop] > dist:
                        min_bus[stop] = dist
                        flag = True

        return min_bus[target] if min_bus[target] < float('inf') else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))
    print(solution.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 8, 6))
