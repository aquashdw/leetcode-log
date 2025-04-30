from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        for num in nums:
            if num < target + 1:
                dp[num] += 1

        for i in range(1, target + 1):
            for num in nums:
                if i + num > target:
                    continue
                dp[i + num] += dp[i]

        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum4([1, 2, 3], 4))
    print(solution.combinationSum4([9], 3))
