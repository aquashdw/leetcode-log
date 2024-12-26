from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        front = 0
        back = len(nums) - 1
        while front <= back:
            mid = (front + back) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                front = mid + 1
            else:
                back = mid - 1

        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
    print(solution.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
