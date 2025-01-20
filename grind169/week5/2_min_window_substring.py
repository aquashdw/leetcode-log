class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = {}
        for c in t:
            if c not in required.keys():
                required[c] = 0
            required[c] += 1

        used = {
            c: 0 for c in required
        }

        n = len(s)
        front = 0
        back = 0
        min_range = [-10000, 10000]
        while back < n:
            if s[back] in used:
                used[s[back]] += 1
            back += 1
            while front < back and self.check_valid(required, used):
                if back - front < min_range[1] - min_range[0]:
                    min_range[0] = front
                    min_range[1] = back
                if s[front] in used:
                    used[s[front]] -= 1
                front += 1
        if min_range[0] == -10000:
            return ""
        return s[min_range[0]:min_range[1]]

    def check_valid(self, required, used):
        for key in used:
            if required.get(key, 0) > used.get(key, 0):
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow("ADOBECODEBANC", "ABC"))
    print(solution.minWindow("a", "a"))
    print(solution.minWindow("a", "aa"))
