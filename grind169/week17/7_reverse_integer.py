from collections import deque


class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return x
        minus = x < 0
        x = abs(x)
        ceil = [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]
        queue = deque()
        while x:
            queue.append(x % 10)
            x //= 10

        while queue[-1] == 0:
            queue.pop()

        if len(queue) > len(ceil):
            return 0

        danger = len(queue) == len(ceil)

        result = 0
        idx = 0
        while len(queue) > 0:
            result *= 10
            now = queue.popleft()
            if danger:
                if now > ceil[idx]:
                    return 0
                elif now < ceil[idx]:
                    danger = False
                else:
                    idx += 1
            result += now

        return -result if minus else result


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(int(input())))
