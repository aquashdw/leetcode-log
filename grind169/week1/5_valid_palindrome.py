class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        front = 0
        back = len(s) - 1

        while front < len(s) and not s[front].isalnum():
            front += 1
        while back > -1 and not s[back].isalnum():
            back -= 1

        while front < back:
            if s[front] != s[back]:
                return False
            front += 1
            back -= 1
            while front < len(s) and not s[front].isalnum():
                front += 1
            while back > -1 and not s[back].isalnum():
                back -= 1

        return True


if __name__ == '__main__':
    print(Solution().isPalindrome(" "))
