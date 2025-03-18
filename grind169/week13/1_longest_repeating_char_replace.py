from collections import deque


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = set(list(s))
        n = len(s)
        max_consecutive = 0
        for char in letters:
            change_idx = deque()
            consecutive = 0
            for i in range(n):
                if s[i] != char:
                    change_idx.append(i)
                    if len(change_idx) > k:
                        consecutive = i - change_idx.popleft()
                        consecutive -= 1

                consecutive += 1
                max_consecutive = max(max_consecutive, consecutive)

        return max_consecutive


if __name__ == '__main__':
    solution = Solution()
    print(solution.characterReplacement('ABAB', 2))
    print(solution.characterReplacement('ABCB', 2))
    print(solution.characterReplacement('AABABBA', 1))
