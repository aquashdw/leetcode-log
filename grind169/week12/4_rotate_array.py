from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        if k:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums, 3)
    print(nums)
    nums = [-1, -100, 3, 99]
    solution.rotate(nums, 2)
    print(nums)
