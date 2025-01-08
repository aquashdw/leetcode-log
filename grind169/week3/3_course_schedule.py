from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = [0 for _ in range(numCourses)]
        adj_list = [[] for _ in range(numCourses)]
        for pre_req in prerequisites:
            adj_list[pre_req[1]].append(pre_req[0])
            in_degrees[pre_req[0]] += 1

        to_visit = deque()
        for idx, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                to_visit.append(idx)

        while to_visit:
            now = to_visit.popleft()
            for next in adj_list[now]:
                in_degrees[next] -= 1
                if in_degrees[next] == 0:
                    to_visit.append(next)

        for in_degree in in_degrees:
            if in_degree != 0:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(2, [[1, 0]]))
    print(solution.canFinish(2, [[1, 0], [0, 1]]))
