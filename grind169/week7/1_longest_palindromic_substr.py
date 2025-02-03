class Solution:
    """
    # BF from longest possible
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        for long in range(length, 0, -1):
            for start in range(0, length - long + 1):
                end = start + long - 1
                front, back = start, end
                fail = False
                while front < back:
                    if s[front] != s[back]:
                        fail = True
                        break
                    front += 1
                    back -= 1
                if fail:
                    continue
                return s[start:end + 1]
        return s[0]
    """

    # BF expand from center
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        max_palindrome = s[0]
        max_length = 1

        for i in range(length):
            left, right = i - 1, i + 1
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            current_length = right - left - 1
            # aba -> -1, 3
            if current_length > max_length:
                max_palindrome = s[left + 1:right]
                max_length = current_length

            left, right = i, i + 1
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            current_length = right - left - 1
            if current_length > max_length:
                max_palindrome = s[left + 1:right]
                max_length = current_length

        return max_palindrome


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("babad"))
    print(solution.longestPalindrome("asdfdsa"))
    print(solution.longestPalindrome("cbbd"))
    print(solution.longestPalindrome("asdfqwerasdf"))
