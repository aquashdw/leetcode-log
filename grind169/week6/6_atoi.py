class Solution:
    low = -2147483648
    high = 2147483647

    def myAtoi(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        idx = 0
        while idx < n and s[idx] == ' ':
            idx += 1
        if n == idx:
            return 0

        negative = False
        if s[idx] == '-':
            negative = True
            idx += 1
        elif s[idx] == '+':
            idx += 1

        result = 0
        while idx < n:
            if not s[idx].isdigit():
                break
            result *= 10
            result += -int(s[idx]) if negative else int(s[idx])
            if result > self.high or result < self.low:
                return self.low if negative else self.high
            idx += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi("42"))
    print(solution.myAtoi("   -042"))
    print(solution.myAtoi("1337c0d3"))
    print(solution.myAtoi("0-1"))
    print(solution.myAtoi("words and 987"))
