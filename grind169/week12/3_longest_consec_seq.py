from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        filtered = set(nums)
        max_len = 0
        for num in filtered:
            if num - 1 in filtered:
                continue

            end = num + 1
            while end in filtered:
                end += 1

            max_len = max(max_len, end - num)
        return max_len


if __name__ == '__main__':
    solution = Solution()
