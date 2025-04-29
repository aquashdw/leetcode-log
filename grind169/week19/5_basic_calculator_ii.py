class Solution:
    def __init__(self):
        self.operators = {"+", "-", "*", "/"}
        self.priority = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def calculate(self, s: str) -> int:
        s = s.strip()
        s = s.replace(" ", "")
        for operator in self.operators:
            s = s.replace(f"{operator}", f" {operator} ")
        infix_expr = s.split(" ")
        stack = []
        postfix_expr = []
        for token in infix_expr:
            if token not in self.operators:
                postfix_expr.append(int(token))
                continue

            if not stack:
                stack.append(token)
                continue

            while stack and self.priority[stack[-1]] >= self.priority[token]:
                postfix_expr.append(stack.pop())
            stack.append(token)
        while stack:
            postfix_expr.append(stack.pop())

        for token in postfix_expr:
            if type(token) == int:
                stack.append(token)
                continue

            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            elif token == "/":
                stack.append(left // right)

        return stack.pop()


if __name__ == '__main__':
    solution = Solution()
    # print(solution.calculate("3+2*2"))
    print(solution.calculate(" 3+5 / 2 "))
