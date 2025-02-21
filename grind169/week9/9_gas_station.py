from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        fills = [gas[i] - cost[i] for i in range(len(gas))]
        diffs = [fills[0]]
        min_idx = 0
        for i in range(len(gas) - 1):
            diffs.append(diffs[i] + fills[i + 1])
            if diffs[i + 1] < diffs[min_idx]:
                min_idx = i + 1

        if diffs[-1] < 0:
            return -1

        return (min_idx + 1) % len(gas)


if __name__ == '__main__':
    solution = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    for i in range(5):
        print((8 - i) % 5)
        print(solution.canCompleteCircuit(gas, cost))
        gas.append(gas.pop(0))
        cost.append(cost.pop(0))
        print()
    # print(solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    # print(solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
