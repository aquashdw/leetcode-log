from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = sorted(coins)
        dp = [10001 for _ in range(amount + 1)]
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    break
                if i == coin:
                    dp[i] = 1
                    continue
                diff = i - coin
                if dp[diff] == 10001:
                    continue
                dp[i] = min(dp[diff] + 1, dp[i])
        return dp[amount] if dp[amount] != 10001 else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 11))
    print(solution.coinChange([2], 3))
    print(solution.coinChange([1], 0))
