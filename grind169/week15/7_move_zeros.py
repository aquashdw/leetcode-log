from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pulls = [0 for _ in range(len(nums))]
        zeros = 0
        for idx, num in enumerate(nums):
            if num == 0:
                zeros += 1
            else:
                pulls[idx] = zeros

        for idx in range(len(nums)):
            swap = idx - pulls[idx]
            nums[swap], nums[idx] = nums[idx], nums[swap]


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(nums)
    nums = [0]
    solution.moveZeroes(nums)
    print(nums)
