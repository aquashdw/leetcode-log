class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n % 2
            n //= 2
        return count

    # def hammingWeight(self, n: int) -> int:
    #     count = 0
    #     bit = 1
    #     while bit <= n:
    #         count += 1 if n & bit else 0
    #         bit <<= 1
    #
    #     return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingWeight(11))
    print(solution.hammingWeight(128))
    print(solution.hammingWeight(2147483645))
