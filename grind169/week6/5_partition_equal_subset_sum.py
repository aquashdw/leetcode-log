from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        if num_sum % 2 != 0:
            return False

        target = num_sum // 2
        nums.sort()
        dp = [False for _ in range(target + 1)]
        dp[0] = True
        for num in nums:
            if num > target:
                break
            for i in range(target, -1, -1):
                if dp[i] and i + num <= target:
                    dp[i + num] = True
            dp[num] = True

        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.canPartition([1, 5, 11, 5]))
    print(solution.canPartition([1, 2, 3, 5]))
    print(solution.canPartition([1, 2, 5]))
