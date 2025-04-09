from typing import List


class Solution:
    deltas = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {
            'refs': 0,
            'word': False,
            'children': {},
        }

        def add_word(word):
            node = trie
            node['refs'] += 1
            for letter in word:
                children = node['children']
                if letter not in children:
                    children[letter] = {
                        'refs': 0,
                        'word': False,
                        'children': {},
                    }
                node = children[letter]
                node['refs'] += 1
            node['word'] = True

        for word in words:
            add_word(word)

        def remove_word(word):
            node = trie
            node['refs'] -= 1
            for letter in word:
                children = node['children']
                if letter in children:
                    node = children[letter]
                    node['refs'] -= 1

        width = len(board[0])
        height = len(board)

        visited = [[False for _ in range(width)] for _ in range(height)]
        check_bounds = lambda y, x: 0 <= x < width and 0 <= y < height
        found = []

        def dfs(now_y, now_x, trie_node, building):
            children = trie_node['children']
            now_letter = board[now_y][now_x]
            if now_letter not in children or \
                    children[now_letter]['refs'] < 1:
                return

            visited[now_y][now_x] = True
            node = children[now_letter]
            building.append(now_letter)
            if node['word']:
                node['word'] = False
                found.append(''.join(building))
                remove_word(found[-1])

            for delta in self.deltas:
                next_y = now_y + delta[0]
                next_x = now_x + delta[1]
                if check_bounds(next_y, next_x) and not visited[next_y][next_x]:
                    dfs(next_y, next_x, node, building)
            visited[now_y][now_x] = False
            building.pop()

        for i in range(height):
            for j in range(width):
                dfs(i, j, trie, [])

        return found


if __name__ == '__main__':
    solution = Solution()
    print(solution.findWords(
        [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
        ["oath", "pea", "eat", "rain"],
    ))
    print(solution.findWords(
        [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
        ["oath", "pea", "eat", "rain", "hklf", "hf"],
    ))
