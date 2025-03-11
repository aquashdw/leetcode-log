from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return s

        store = deque()
        int_queue = deque()
        char_queue = deque()
        for char in s:
            if char.isalpha():
                store.append(char)
            elif char.isdigit():
                int_queue.append(int(char))
            elif char == '[':
                repeat = 0
                while int_queue:
                    repeat *= 10
                    repeat += int_queue.popleft()
                store.append(repeat)
                store.append('[')
            else:  # elif char == ']':
                while store and store[-1] != '[':
                    char_queue.appendleft(store.pop())
                block = ''.join(char_queue)
                char_queue.clear()
                store.pop()
                repeat = store.pop()
                store.append(block * repeat)

        return ''.join(store)


if __name__ == '__main__':
    solution = Solution()
    print(solution.decodeString("3[a]2[bc]"))
    print(solution.decodeString("3[a2[c]]"))
    print(solution.decodeString("2[abc]3[cd]ef"))
