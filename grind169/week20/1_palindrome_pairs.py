from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if not words:
            return []

        def is_palindrome(target):
            n = len(target)
            for i in range(n // 2):
                if target[i] != target[n - 1 - i]:
                    return False
            return True

        results = []
        word_map = {words[i]: i for i in range(len(words))}
        if "" in word_map:
            blank_idx = word_map[""]
            for idx, word in enumerate(words):
                if word == "":
                    continue
                if is_palindrome(word):
                    results.append([blank_idx, idx])
                    results.append([idx, blank_idx])

        for idx, word in enumerate(words):
            word_rev = word[::-1]
            if word_rev in word_map and word_map[word_rev] != idx:
                results.append([idx, word_map[word_rev]])

        for idx, word in enumerate(words):
            for bound in range(1, len(word)):
                if is_palindrome(word[:bound]):
                    part_rev = word[:bound - 1:-1]
                    if part_rev in word_map:
                        if word_map[part_rev] == idx:
                            continue
                        results.append([word_map[part_rev], idx])
                if is_palindrome(word[bound:]):
                    part_rev = word[bound - 1::-1]
                    if part_rev in word_map:
                        if word_map[part_rev] == idx:
                            continue
                        results.append([idx, word_map[part_rev]])

        return results


if __name__ == '__main__':
    solution = Solution()
    # print(solution.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
    print(solution.palindromePairs(["bb", "bababab", "baab", "abaabaa", "aaba", "", "bbaa", "aba", "baa", "b"]))
