from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.nums = []
        self.n = 0
        self.used = []
        self.perm = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.nums = nums
        self.n = len(nums)
        self.used = [False for _ in range(self.n)]
        self.perm = []
        self.recur(0)
        return self.result

    def recur(self, next: int):
        if next == self.n:
            self.result.append(self.perm.copy())
            return

        for i in range(self.n):
            if self.used[i]:
                continue
            self.used[i] = True
            self.perm.append(self.nums[i])
            self.recur(next + 1)
            self.used[i] = False
            self.perm.pop()


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
    print(solution.permute([]))
