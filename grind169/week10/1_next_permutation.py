from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        for k in range(1, (n - i) // 2 + 1):
            nums[i + k], nums[n - k] = nums[n - k], nums[i + k]


if __name__ == '__main__':
    solution = Solution()
    # nums = [1, 3, 2]
    nums = [1, 4, 2, 3]
    solution.nextPermutation(nums)
    print(nums)
