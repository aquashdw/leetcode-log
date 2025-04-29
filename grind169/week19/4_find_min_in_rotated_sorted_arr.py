from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            if left + 1 == right or left + 2 == right:
                return min(nums[left:right + 1])
            mid = (left + right) // 2
            left_direct = nums[left] < nums[mid]
            right_direct = nums[mid + 1] < nums[right]
            if left_direct and right_direct:
                return min(nums[left], nums[mid + 1])

            if left_direct:
                left = mid + 1
            else:
                right = mid
        return min(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMin([2, 1]))
    print(solution.findMin([3, 4, 5, 1, 2]))
    print(solution.findMin([4, 5, 6, 7, 0, 1, 2, 3]))
    print(solution.findMin([11, 13, 15, 17]))

"""

0 1 2 3 | 4 5 6 7

7 0 | 1 2 | 3 4 5 6

6 7 | 0 1 | 2 3 4 5

5 6 | 7 0 | 1 2 3 4

4 5 6 7 | 0 1 2 3

3 4 5 6 | 7 0 | 1 2

2 3 4 5 | 6 7 | 0 1

1 2 3 4 | 5 6 | 7 0

"""

"""

1 2 3 | 4 5

5 | 1 2 | 3 4

4 | 5 1 | 2 3

3 4 5 | 1 2

2 3 4 | 5 1

"""
