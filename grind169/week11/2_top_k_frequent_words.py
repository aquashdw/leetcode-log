from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count_dict = defaultdict(lambda: 0)
        for word in words:
            count_dict[word] += 1

        return sorted(count_dict.keys(), key=lambda x: (-count_dict[x], x))[:k]


if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
