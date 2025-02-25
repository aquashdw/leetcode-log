from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        sub_max = 1
        sub_min = 1

        for num in nums:
            product = sub_max * num
            sub_max = max(product, sub_min * num, num)
            sub_min = min(product, sub_min * num, num)

            result = max(result, sub_max)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct([2, 3, -2, 4]))
