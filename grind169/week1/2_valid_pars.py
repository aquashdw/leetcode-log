class Solution:
    opens = ["(", "{", "["]
    close = [")", "}", "]"]

    def isValid(self, s: str) -> bool:
        stack = []
        for par in s:
            if par in self.opens:
                stack.append(par)
                continue

            if not stack:
                return False

            if self.opens.index(stack.pop()) != self.close.index(par):
                return False

        return not stack


if __name__ == '__main__':
    print(Solution().isValid("(]"))
