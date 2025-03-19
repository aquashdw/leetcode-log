from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = [False for _ in range(n)]
        visited[0] = True
        idx = 0
        while not visited[-1] and idx < n:
            if visited[idx]:
                far_range = idx + nums[idx]
                far_range = far_range if far_range < n else n - 1
                if not visited[far_range]:
                    for reach in range(idx + 1, far_range + 1):
                        visited[reach] = True
            idx += 1

        return visited[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.canJump([2, 3, 1, 1, 4]))
    print(solution.canJump([3, 2, 1, 0, 4]))
