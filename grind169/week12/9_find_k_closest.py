from collections import deque
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []
        front = 0
        back = len(arr) - 1
        mid = 0
        while front <= back:
            mid = (front + back) // 2

            if arr[mid] == x:
                break
            elif arr[mid] < x:
                front = mid + 1
            else:
                back = mid - 1

        left = right = mid
        if arr[mid] <= x:
            right += 1
        elif arr[mid] > x:
            left -= 1
        result = deque()
        while len(result) < k:
            if left == -1:
                result.append(arr[right])
                right += 1
                continue
            if right == len(arr):
                result.appendleft(arr[left])
                left -= 1
                continue

            left_diff = abs(x - arr[left])
            right_diff = abs(arr[right] - x)
            if right_diff < left_diff:
                result.append(arr[right])
                right += 1
            else:
                result.appendleft(arr[left])
                left -= 1

        return list(result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findClosestElements([1, 2, 3, 4, 5], 4, 3))
    print(solution.findClosestElements([1, 2, 3, 4, 5], 4, 6))
    print(solution.findClosestElements([1, 2, 3, 4, 5], 2, 4))
    print(solution.findClosestElements([3, 6, 9, 12, 15], 2, 13))
    print(solution.findClosestElements([1, 1, 2, 3, 4, 5], 4, -1))
    print(solution.findClosestElements([1, 3], 1, 2))  # mid = 1
    print(solution.findClosestElements([1, 5, 10], 1, 4))  # mid = 0
