from typing import List


class Solution:
    def __init__(self):
        self.results = None

    def dfs(self, generating, open_pars, close_pars):
        if open_pars == close_pars == 0:
            self.results.append(''.join(generating))
            return

        if close_pars > open_pars:
            generating.append(')')
            self.dfs(generating, open_pars, close_pars - 1)
            generating.pop()
        if open_pars > 0:
            generating.append('(')
            self.dfs(generating, open_pars - 1, close_pars)
            generating.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.results = []
        self.dfs([], n, n)
        return self.results


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(1))
    print(solution.generateParenthesis(2))
    print(solution.generateParenthesis(3))
    print(solution.generateParenthesis(8))
