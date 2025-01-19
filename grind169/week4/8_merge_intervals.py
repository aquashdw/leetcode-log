from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        current = intervals[0]
        result = []
        for i in range(1, len(intervals)):
            now = intervals[i]
            if now[0] <= current[1]:
                current[1] = max(current[1], now[1])
            else:
                result.append(current)
                current = now
        result.append(current)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(solution.merge([[1, 4], [4, 5]]))
