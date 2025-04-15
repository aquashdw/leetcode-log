class Solution:
    # def __init__(self):
    #     self.count = 0
    #     self.str = ''
    #     self.len = 0
    #
    # def numDecodings(self, s: str) -> int:
    #     self.count = 0
    #     self.str = s
    #     self.len = len(s)
    #     self.dfs(0)
    #     return self.count
    #
    # def dfs(self, start):
    #     if start == self.len:
    #         self.count += 1
    #         return
    #
    #     if self.str[start] == '0':
    #         return
    #
    #     self.dfs(start + 1)
    #
    #     if start + 1 < self.len and int(self.str[start:start + 2]) < 27:
    #         self.dfs(start + 2)

    def numDecodings(self, s: str) -> int:
        # if the first is 0 it is not feasible
        if s[0] == '0':
            return 0
        n = len(s)
        if n == 1:
            return 1
        # dp[i] keeps track of valid cases of decoding up to ith digit
        dp = [0 for _ in range(n)]
        # use the first digit to decode
        dp[0] = 1
        # if the first two digits are less than 27 then there are two cases:
        # (s[0], s[1]), (s[0:1])
        dp[1] += 1 if s[1] != '0' else 0
        dp[1] += 1 if int(s[0:2]) < 27 else 0

        # if s[i-1:i+1] is over 10 and less than 27, then for all cases for dp[i-2] we can use s[i-1:i+1] for decoding
        # if s[i] is not 0, then for all cases for dp[i-1] we can use s[i] for decoding
        # if s[i] is 0 and s[i-1:i+1] is over 26, then it is not feasible
        for i in range(2, n):
            double_digit = int(s[i - 1:i + 1])
            if s[i] == 0 and double_digit > 26:
                return 0
            if 9 < double_digit < 27:
                dp[i] += dp[i - 2]
            if '0' < s[i]:
                dp[i] += dp[i - 1]
        # print(dp)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numDecodings('12'))
    print(solution.numDecodings('226'))
    print(solution.numDecodings('06'))
    print(solution.numDecodings('2611055971756562'))
    print(solution.numDecodings('111111111111111111111111111111111111111111111'))
    print(solution.numDecodings('10'))
