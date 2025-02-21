from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [
            [nums[0], nums[1]],
            [0, nums[0]],
        ]

        for i in range(2, n):
            dp[0].append(max(dp[0][i - 2], dp[1][i - 1]) + nums[i])
            dp[1].append(max(dp[0][i - 1], dp[1][i - 1]))

        return max(dp[0][-1], dp[1][-1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([1, 2, 3, 1]))
    print(solution.rob([2, 7, 9, 3, 1]))
    print(solution.rob([1, 100, 1, 0, 1, 0]))
