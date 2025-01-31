from typing import List


class Solution:
    def __init__(self):
        self.source = ''
        self.length = 0
        self.word_dict = None
        self.memo = set()

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.source = s
        self.length = len(self.source)
        self.word_dict = wordDict
        self.word_dict.sort(key=lambda x: -len(x))
        return self.segment(0)

    def segment(self, idx):
        if idx in self.memo:
            return False
        if idx == len(self.source):
            return True

        for word in self.word_dict:
            if self.compare(idx, word) and self.segment(idx + len(word)):
                return True

        self.memo.add(idx)
        return False

    def compare(self, start_idx, word):
        word_len = len(word)
        if word_len + start_idx > self.length:
            return False

        for i in range(word_len):
            if self.source[start_idx + i] != word[i]:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordBreak("applepenapple", ["apple", "pen"]))
    print(solution.wordBreak("leetcode", ["leet", "code"]))
    print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(solution.wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
