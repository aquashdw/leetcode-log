class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        stack = []
        valid = [False for _ in range(len(s))]
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stack.append(i)

            elif char == ')' and stack:
                last_open = stack.pop()
                valid[i] = True
                valid[last_open] = True

            else:
                stack.clear()

        max_length = 0
        length = 0
        for v in valid:
            if v:
                length += 1
                max_length = max(length, max_length)
            else:
                length = 0

        return max_length


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestValidParentheses('(()'))
    print(solution.longestValidParentheses(')()())'))
    print(solution.longestValidParentheses('()(())'))
    print(solution.longestValidParentheses('(()())'))
