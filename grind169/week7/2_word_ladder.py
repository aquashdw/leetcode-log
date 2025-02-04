from collections import deque
from typing import List


class Solution:
    """
    # make adj_list then bfs
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        word_len = len(beginWord)
        words_count = len(wordList) + 1
        words = [beginWord]
        words.extend(wordList)

        adj_list = [[] for _ in range(words_count)]
        goal = -1
        for i in range(words_count):
            if words[i] == endWord:
                goal = i
            for j in range(i + 1, words_count):
                word_a = words[i]
                word_b = words[j]
                diff = 0
                for idx in range(word_len):
                    if word_a[idx] != word_b[idx]:
                        diff += 1
                    if diff > 1:
                        break
                else:
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        visited = [False for _ in range(words_count)]
        visited[0] = True
        to_visit = deque()
        to_visit.append((0, 1))
        while to_visit:
            now, dist = to_visit.popleft()
            for go_next in adj_list[now]:
                if visited[go_next]:
                    continue
                visited[go_next] = True
                if go_next == goal:
                    return dist + 1
                to_visit.append((go_next, dist + 1))
        return 0
    """

    # keep track as set
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        word_len = len(beginWord)
        offset = ord('a')
        to_visit = deque()
        to_visit.append((beginWord, 1))
        while to_visit:
            now, dist = to_visit.popleft()
            for i in range(word_len):
                for alpha in range(26):
                    next_word = now[:i] + chr(offset + alpha) + now[i + 1:]
                    if next_word == endWord:
                        return dist + 1
                    if next_word in word_set:
                        word_set.remove(next_word)
                        to_visit.append((next_word, dist + 1))

        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.ladderLength("hit", "cog",["hot","dot","dog","lot","log","cog"]))