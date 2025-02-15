from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj_list = [
            [] for _ in range(n)
        ]
        degrees = [0 for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
            degrees[edge[0]] += 1
            degrees[edge[1]] += 1

        now_queue = deque([i for i in range(n) if degrees[i] == 1])
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(now_queue)
            next_queue = deque()
            while now_queue:
                now = now_queue.popleft()
                for next_v in adj_list[now]:
                    degrees[next_v] -= 1
                    if degrees[next_v] == 1:
                        next_queue.append(next_v)
            now_queue = next_queue

        return list(now_queue)
