from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_strs = list(map(str, nums))
        num_strs.sort(key=cmp_to_key(lambda x, y: -1 if x + y > y + x else 1))
        if num_strs[0] == '0':
            return '0'
        return "".join(num_strs)


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestNumber([10, 2]))
    print(solution.largestNumber([3, 30, 34, 5, 9]))
    print(solution.largestNumber([0, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(solution.largestNumber([0, 0]))
