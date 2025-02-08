from bisect import bisect_right
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        works = list(zip(startTime, endTime, profit))
        works.sort(key=lambda x: x[1])
        n = len(works)
        dp = [0 for _ in range(n + 1)]
        for i, (start_time, _, current_profit) in enumerate(works):
            index = bisect_right(works, start_time, hi=i, key=lambda x: x[1])
            dp[i + 1] = max(dp[i], dp[index] + current_profit)

        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
