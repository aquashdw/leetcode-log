from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or len(s) < len(p):
            return []
        find_len = len(p)
        front = 0
        back = front + find_len
        pat_dict = defaultdict(lambda: 0)
        for char in p:
            pat_dict[char] += 1

        found_dict = defaultdict(lambda: 0)
        for i in range(back):
            found_dict[s[i]] += 1

        results = []
        for char in pat_dict:
            if pat_dict[char] != found_dict[char]:
                break
        else:
            results.append(0)

        for i in range(len(s) - find_len):
            found_dict[s[i]] -= 1
            found_dict[s[i + find_len]] += 1
            for char in pat_dict:
                if pat_dict[char] != found_dict[char]:
                    break
            else:
                results.append(i + 1)

        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.findAnagrams("cbaebabacd", "abc"))
    print(solution.findAnagrams("abab", "ab"))
    print(solution.findAnagrams("a", "a"))
