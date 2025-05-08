from heapq import heappush, heappop
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        heap = []
        push = lambda item: heappush(heap, item)
        pop = lambda: heappop(heap)

        local_min = float('inf')
        local_max = -float('inf')

        for i in range(n):
            local_min = min(nums[i][0], local_min)
            local_max = max(nums[i][0], local_max)
            push((nums[i][0], i, 0))

        smallest_range = [local_min, local_max]

        while heap:
            local_min, list_idx, item_idx = pop()
            if local_max - local_min < smallest_range[1] - smallest_range[0]:
                smallest_range[0] = local_min
                smallest_range[1] = local_max

            if item_idx >= len(nums[list_idx]) - 1:
                break

            next_item_idx = item_idx + 1
            next_val = nums[list_idx][next_item_idx]
            local_max = max(local_max, next_val)
            push((next_val, list_idx, next_item_idx))

        return smallest_range


if __name__ == '__main__':
    # nums = [
    #     [4, 10, 15, 24, 26],
    #     [0, 9, 12, 20, 23],
    #     [5, 18, 22, 30],
    # ]
    # nums = [[-41, 16, 35, 49, 68, 74, 75], [0, 23, 77, 77, 78], [-27, 85, 92, 93], [-42, 22, 92, 93, 97, 97, 97, 98],
    #         [58], [-58, 34, 52, 54, 55], [-1, 5, 28, 34, 36], [-11, 10, 52, 57, 61], [29, 52, 54],
    #         [-46, -4, -3, 27, 44, 46, 49, 53, 54, 54, 54, 54, 54, 54, 54, 54, 55]]
    nums = [[-59, -37, -12, 39, 83, 83, 83, 84], [-38, 40, 64, 75, 86, 87, 89, 90], [-4, 9, 41, 57, 69, 71, 72],
            [-8, 13, 24, 27], [18]]
    solution = Solution()
    print(solution.smallestRange(nums))
    # 4, 0, 5 => [0, 5]
    # 4, 9, 5 => [4, 9]
    # 10, 9, 5 => [5, 10]
    # 10, 9, 18 => [9, 18]
    # 10, 12, 18 => [10, 18]
    # 15, 12, 18 => [12, 18]
    # 15, 20, 18 => [15, 20]
    # 24, 20, 18 => [18, 24]
    # 24, 20, 22 => [20, 24]
    # 24, 23, 22 => [22, 24]
    # 24, 23, 30 => [23, 30]
