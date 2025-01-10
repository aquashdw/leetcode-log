from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0 for _ in range(n)]
        answer[0] = 1
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        inverse = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= inverse
            inverse *= nums[i]

        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))
    print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
