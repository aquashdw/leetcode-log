class Solution:
    """
    dictionary (hash table)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = dict()
        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
            counts[t[i]] = counts.get(t[i], 0) - 1

        for value in counts.values():
            if value != 0:
                return False
        return True
    """

    # ascii count
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = [0 for _ in range(26)]
        ord_a = ord("a")
        for i in range(len(s)):
            counts[ord(s[i]) - ord_a] += 1
            counts[ord(t[i]) - ord_a] -= 1

        for count in counts:
            if count != 0:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram(s="anagram", t="nagaram"))
    print(solution.isAnagram(s="rat", t="car"))
