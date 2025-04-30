from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        last_end = -float('inf')
        remove = 0
        for interval in intervals:
            if interval[0] < last_end:
                remove += 1
                continue
            last_end = interval[1]

        return remove


if __name__ == '__main__':
    solution = Solution()
    print(solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(solution.eraseOverlapIntervals([[1, 2], [2, 3]]))
