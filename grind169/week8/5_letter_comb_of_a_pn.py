from typing import List


class Solution:
    def __init__(self):
        self.digit_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        results = []
        self.permutate(digits, 0, [], results)
        return results

    def permutate(self, digits, now, selected, results):
        if now == len(digits):
            results.append(''.join(selected))
            return
        digit_now = digits[now]
        digit_letters = self.digit_letters[digit_now]
        for i in range(len(digit_letters)):
            selected.append(digit_letters[i])
            self.permutate(digits, now + 1, selected, results)
            selected.pop()


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations('23'))
