from typing import List


def is_palindrome(word, start, end):
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True


class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = None
        self.list = []

    def insert(self, word: str, idx: int) -> None:
        node = self
        for i in range(len(word) - 1, -1, -1):
            char = word[i]
            if char not in node.children:
                node.children[char] = TrieNode()
            if is_palindrome(word, 0, i):
                node.list.append(idx)
            node = node.children[char]
        node.list.append(idx)
        node.idx = idx


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if not words:
            return []

        results = []
        root = TrieNode()
        for idx, word in enumerate(words):
            root.insert(word, idx)

        def search_pairs(idx):
            node = root
            word = words[idx]
            word_len = len(word)
            for i in range(word_len):
                if node.idx is not None and node.idx != idx and is_palindrome(word, i, word_len - 1):
                    results.append([idx, node.idx])

                if word[i] not in node.children:
                    return
                node = node.children[word[i]]

            for i in node.list:
                if i != idx:
                    results.append([idx, i])

        for idx in range(len(words)):
            search_pairs(idx)

        return results


if __name__ == '__main__':
    solution = Solution()
    # print(solution.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
    print(solution.palindromePairs(["bb", "bababab", "baab", "abaabaa", "aaba", "", "bbaa", "aba", "baa", "b"]))
