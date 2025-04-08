from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = []
        for row in matrix:
            flattened.extend(row)

        front = 0
        back = len(flattened) - 1
        while front <= back:
            mid = (front + back) // 2

            if flattened[mid] == target:
                return True
            elif flattened[mid] < target:
                front = mid + 1
            else:
                back = mid - 1

        return False
