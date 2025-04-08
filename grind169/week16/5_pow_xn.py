class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n *= -1
            x = 1 / x

        result = 1
        while n > 0:
            if n % 2:
                result *= x
                n -= 1
            x *= x
            n //= 2
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(2.0, 10))
    print(solution.myPow(2.1, 3))
    print(solution.myPow(2.0, -2))
