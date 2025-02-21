from collections import deque


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_in = deque()
        t_in = deque()

        for i in range(len(s)):
            if s[i] != '#':
                s_in.append(s[i])
                continue

            if s_in:
                s_in.pop()

        for i in range(len(t)):
            if t[i] != '#':
                t_in.append(t[i])
                continue

            if t_in:
                t_in.pop()

        while s_in and t_in:
            s_next = s_in.popleft()
            t_next = t_in.popleft()
            if s_next != t_next:
                return False

        if s_in or t_in:
            return False

        return True
