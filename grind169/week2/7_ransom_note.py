class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        used = [0 for _ in range(26)]
        for a in ransomNote:
            used[ord(a) - ord('a')] += 1
        for a in magazine:
            used[ord(a) - ord('a')] -= 1

        for i in used:
            if i > 0:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.canConstruct(ransomNote="a", magazine="b"))
