from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            min_height = min(height[left], height[right])
            max_area = max(max_area, (right - left) * min_height)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
