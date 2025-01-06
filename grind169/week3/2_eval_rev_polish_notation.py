from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operators:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    sign = 1 if (left >= 0 and right > 0) or (left <= 0 and right < 0) else - 1
                    stack.append((abs(left) // abs(right)) * sign)
            else:
                stack.append(int(token))
        return stack.pop()


if __name__ == '__main__':
    solution = Solution()
    # print(solution.evalRPN(["2", "1", "+", "3", "*"]))
    # print(solution.evalRPN(["4", "13", "5", "/", "+"]))
    print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
