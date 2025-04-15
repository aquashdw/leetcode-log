from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        real_sum = sum(i for i in range(n + 1))
        return real_sum - sum(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.missingNumber([3, 0, 1]))
    print(solution.missingNumber([0, 1]))
    print(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
