from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res_diff = -float('inf')
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            remaining = target - nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                now = nums[left] + nums[right]
                if now == remaining:
                    return target

                diff = nums[i] + now - target
                if abs(diff) < abs(res_diff):
                    res_diff = diff

                # target > 3sum
                if diff < 0:
                    left += 1
                # target < 3sum
                else:
                    right -= 1

        return target + res_diff


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest([-1, 2, 1, -4], 1))
    print(solution.threeSumClosest([0, 0, 0], 1))
