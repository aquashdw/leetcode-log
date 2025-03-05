from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        in_degrees = [0 for _ in range(numCourses)]
        for prerequisite in prerequisites:
            in_degrees[prerequisite[0]] += 1
            adj_list[prerequisite[1]].append(prerequisite[0])

        queue = deque()
        for i in range(numCourses):
            if not in_degrees[i]:
                queue.append(i)

        result = []
        while queue:
            now = queue.popleft()
            result.append(now)
            for next_lecture in adj_list[now]:
                in_degrees[next_lecture] -= 1
                if not in_degrees[next_lecture]:
                    queue.append(next_lecture)

        return [] if sum(in_degrees) else result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findOrder(2, [[1, 0]]))
    # print(solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    # print(solution.findOrder(1, []))
    print(solution.findOrder(3, [[1, 0], [1, 2], [0, 1]]))
