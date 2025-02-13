from typing import List


class Solution:
    deltas = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
    ]

    def __init__(self):
        self.board = None
        self.visited = None
        self.word = ''
        self.height = None
        self.width = None

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.height = len(board)
        self.width = len(board[0])
        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]

        starts = []
        for i in range(self.height):
            for j in range(self.width):
                if board[i][j] == word[0]:
                    starts.append((i, j, 1))

        return self.start_dfs(starts)

    def start_dfs(self, starts):
        for start in starts:
            self.visited[start[0]][start[1]] = True
            if self.dfs(start[0], start[1], start[2]):
                return True
            self.visited[start[0]][start[1]] = False
        else:
            return False

    def dfs(self, now_y, now_x, next_i):
        if next_i == len(self.word):
            return True
        for delta in Solution.deltas:
            next_y = now_y + delta[0]
            next_x = now_x + delta[1]
            if (0 <= next_y < self.height and 0 <= next_x < self.width
                    and not self.visited[next_y][next_x]
                    and self.board[next_y][next_x] == self.word[next_i]):
                self.visited[next_y][next_x] = True
                if self.dfs(next_y, next_x, next_i + 1):
                    return True
                self.visited[next_y][next_x] = False
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
    print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
    print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
