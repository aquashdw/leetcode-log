class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        last = 2
        count = 3
        for i in range(n - 3):
            last, count = count, count + last

        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
    print(solution.climbStairs(4))
    print(solution.climbStairs(5))
    print(solution.climbStairs(6))
