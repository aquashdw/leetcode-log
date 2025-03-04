from typing import List


class Solution:
    # dp
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        dp = [0, 1]
        if n == 1:
            return dp
        bound = 4
        before_idx = 0
        while len(dp) <= n:
            dp.append(dp[before_idx] + 1)
            before_idx += 1
            if len(dp) == bound:
                bound *= 2
                before_idx = 0

        return dp

    """
    # bit masking
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            cmp = 1
            count = 0
            while cmp <= i:
                count += 1 if cmp & i else 0
                cmp = cmp << 1
            result.append(count)

        return result
    """


if __name__ == '__main__':
    solution = Solution()
    print(solution.countBits(5))
