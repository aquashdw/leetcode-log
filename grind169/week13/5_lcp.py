from typing import List


class Solution:
    class Solution:
        def longestCommonPrefix(self, strs: List[str]) -> str:
            ceil = min([len(s) for s in strs])
            for i in range(ceil):
                if len(set([s[i] for s in strs])) > 1:
                    end = i
                    break
            else:
                end = ceil

            return strs[0][:end]

    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ceil = min([len(s) for s in strs])
        for i in range(ceil):
            first = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != first:
                    end = i
                    break
            else:
                continue
            break
        else:
            end = ceil

        return strs[0][:end]
    """


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
    print(solution.longestCommonPrefix(["a"]))
