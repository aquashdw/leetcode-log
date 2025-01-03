from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = len(nums)
        answers = []
        for i in range(count - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left = i + 1
            right = count - 1
            while left < right:
                now = nums[left] + nums[right]
                if now == target:
                    answers.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif now < target:
                    left += 1
                else:
                    right -= 1
        return answers


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
