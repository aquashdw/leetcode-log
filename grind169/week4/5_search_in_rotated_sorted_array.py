from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        k = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                k = i + 1
                break

        front = 0
        back = n - 1
        while front <= back:
            mid = (front + back) // 2
            mid_piv = (mid + k) % n
            if nums[mid_piv] == target:
                return mid_piv
            elif nums[mid_piv] < target:
                front = mid + 1
            else:
                back = mid - 1

        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(solution.search([1], 0))
    print(solution.search([3, 1], 1))

"""
0 1 2 4 5 6 7
mid = 3

4 5 6 7 0 1 2 
mid = 0

"""
