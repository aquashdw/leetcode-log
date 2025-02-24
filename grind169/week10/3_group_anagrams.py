from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = defaultdict(list)
        for string in strs:
            ana_dict[''.join(sorted(string))].append(string)

        return list(ana_dict.values())


if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
