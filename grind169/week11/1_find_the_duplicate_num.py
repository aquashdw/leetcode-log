from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[nums[nums[0]]]
        slow = nums[nums[0]]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]

        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return slow


if __name__ == '__main__':
    solution = Solution()
    print(solution.findDuplicate([3, 1, 2, 4, 2]))
