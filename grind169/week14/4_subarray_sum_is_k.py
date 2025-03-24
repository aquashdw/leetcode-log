from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        total = 0
        current = 0
        sub_count = {
            0: 1
        }

        for num in nums:
            current += num
            if current - k in sub_count:
                total += sub_count[current - k]

            sub_count[current] = 1 + sub_count.get(current, 0)

        return total


if __name__ == '__main__':
    solution = Solution()
    print(solution.subarraySum([1, 1, 1], 2))
    print(solution.subarraySum([1, 2, 3], 3))
