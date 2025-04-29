from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = 0
        while pos < n and nums[pos] < 0:
            pos += 1

        neg = pos - 1

        result = []
        while neg >= 0 and pos < n:
            if abs(nums[neg]) < abs(nums[pos]):
                result.append(nums[neg] * nums[neg])
                neg -= 1
            else:
                result.append(nums[pos] * nums[pos])
                pos += 1

        while neg >= 0:
            result.append(nums[neg] * nums[neg])
            neg -= 1

        while pos < n:
            result.append(nums[pos] * nums[pos])
            pos += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortedSquares([-4, -1, 0, 3, 10]))
    print(solution.sortedSquares([1, 2, 3]))
    print(solution.sortedSquares([-3, -2, -1]))
