from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # first try
        # dp = []
        # max_val = -10000
        # for num in nums:
        #     if len(dp) == 0:
        #         dp.append(num)
        #     else:
        #         dp.append(num if num > dp[-1] + num else dp[-1] + num)
        #     max_val = max(dp[-1], max_val)
        # print(dp)
        # return max_val
        current_sum = nums[0]
        current_max = current_sum
        for num in nums[1:]:
            current_sum = num if num > current_sum + num else current_sum + num
            current_max = max(current_sum, current_max)
        return current_max


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solution.maxSubArray(nums=[1, 2]))
    print(solution.maxSubArray(nums=[5, 4, -1, 7, 8]))
