class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        front = 0
        back = 0
        max_length = 0
        used = [False for _ in range(128)]
        while back < len(s):
            if used[ord(s[back])]:
                while s[front] != s[back]:
                    used[ord(s[front])] = False
                    front += 1
                front += 1
            else:
                used[ord(s[back])] = True
            back += 1
            max_length = max(max_length, back - front)
        return max_length


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
    print(solution.lengthOfLongestSubstring("dvdf"))
