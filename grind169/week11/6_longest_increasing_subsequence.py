from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = [nums[0]]

        def binary_search(target):
            left, right = 0, len(result)
            while left <= right:
                mid = (left + right) // 2
                if result[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        for i in range(len(nums)):
            if nums[i] > result[-1]:
                result.append(nums[i])
            else:
                insert = binary_search(nums[i])
                result[insert] = nums[i]

        return len(result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))
    print(solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
