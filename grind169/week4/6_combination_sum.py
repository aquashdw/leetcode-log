from typing import List


class Solution:
    def __init__(self):
        self.results = []
        self.len = 0

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = []
        self.len = len(candidates)
        self.dfs([], candidates, 0, target)
        return self.results

    def dfs(self, used: List[int], candidates: List[int], last_used: int, target: int):
        if target == 0:
            self.results.append(used.copy())
            return
        if target < 0:
            return

        for i in range(last_used, self.len):
            left = target - candidates[i]
            if left < 0:
                continue
            used.append(candidates[i])
            self.dfs(used, candidates, i, left)
            used.pop()


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7], 7))
    print(solution.combinationSum([2], 1))
