from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pos_nums = [num for num in nums if num > 0]
        for num in pos_nums:
            actual_pos = abs(num) - 1
            if actual_pos < len(pos_nums) and pos_nums[actual_pos] > 0:
                pos_nums[actual_pos] *= -1

        for idx, num in enumerate(pos_nums):
            if num > 0:
                return idx + 1

        return len(pos_nums) + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.firstMissingPositive([1, 2, 0]))
    print(solution.firstMissingPositive([3, 4, -1, 1]))
    print(solution.firstMissingPositive([7, 8, 9, 10, 11, 12]))
