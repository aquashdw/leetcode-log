class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        current_num = 0
        sign = 1
        result = 0
        stack = []
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '+' or char == '-':
                result += current_num * sign
                sign = -1 if char == '-' else 1
                current_num = 0
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * current_num
                result *= stack.pop()
                result += stack.pop()
                current_num = 0

        return result + current_num * sign


if __name__ == '__main__':
    solution = Solution()
    print(solution.calculate('1 + 1'))
    print(solution.calculate('-(2 + 3)'))
    print(solution.calculate('-(-2 + 3)'))
    print(solution.calculate('(-1) + (-2)'))