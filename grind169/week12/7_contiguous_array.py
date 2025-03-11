from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diffs = [0]

        lengths = {
            0: -1
        }
        max_length = 0
        for i in range(len(nums)):
            num = nums[i]
            diffs.append(diffs[-1] + (1 if num else -1))
            height = diffs[-1]
            if height in lengths:
                max_length = max(max_length, i - lengths[height])
            else:
                lengths[height] = i

        return max_length


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxLength([0, 1]))
    print(solution.findMaxLength([0, 1, 0]))
    print(solution.findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0]))
    print(solution.findMaxLength([0, 0, 0, 0, 0]))
    print(solution.findMaxLength([1, 1, 1, 1, 1]))
