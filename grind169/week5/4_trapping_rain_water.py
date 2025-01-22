from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        heights = height
        max_height = max(heights)
        area = len(heights)

        trapped = 0
        temp_trap = 0
        current_height = 0
        left_max = 0
        for i in range(area):
            height = heights[i]
            if height >= current_height:
                trapped += temp_trap
                temp_trap = 0
                if height == max_height:
                    left_max = i
                    break
                current_height = height
            else:
                temp_trap += current_height - height

        temp_trap = 0
        current_height = 0
        right_max = area - 1
        for i in range(area - 1, -1, -1):
            height = heights[i]
            if height >= current_height:
                trapped += temp_trap
                temp_trap = 0
                current_height = height
                if height == max_height:
                    right_max = i
                    break
            else:
                temp_trap += current_height - height

        if left_max != right_max:
            for i in range(left_max + 1, right_max):
                trapped += max_height - heights[i]

        return trapped


if __name__ == '__main__':
    solution = Solution()
    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(solution.trap([4, 2, 0, 3, 2, 5]))
    print(solution.trap([2, 0, 2]))
