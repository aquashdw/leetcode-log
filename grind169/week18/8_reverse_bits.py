class Solution:
    def reverseBits(self, n: int) -> int:
        head = 1
        result = 0
        for i in range(32):
            result *= 2
            if head & n:
                result += 1
            head <<= 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBits(0b00000010100101000001111010011100))
