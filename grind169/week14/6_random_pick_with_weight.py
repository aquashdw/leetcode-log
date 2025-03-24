from typing import List
from random import randint


class Solution:

    def __init__(self, w: List[int]):
        self.numbers = w
        self.cum_sum = [self.numbers[0]]
        for i in range(1, len(self.numbers)):
            self.cum_sum.append(self.cum_sum[i - 1] + self.numbers[i])
        self.sum = self.cum_sum[-1]

    # testing code
    """
    def pickIndex(self, pick_weight) -> int:
        front = 0
        back = len(self.cum_sum)
        while front <= back:
            mid = (front + back) // 2
            if self.cum_sum[mid] == pick_weight:
                return mid + 1
            elif self.cum_sum[mid] < pick_weight:
                front = mid + 1
            else:
                back = mid - 1

        return front
    """

    def pickIndex(self) -> int:
        pick_weight = randint(0, self.sum - 1)

        front = 0
        back = len(self.cum_sum)
        while front <= back:
            mid = (front + back) // 2
            if self.cum_sum[mid] == pick_weight:
                return mid + 1
            elif self.cum_sum[mid] < pick_weight:
                front = mid + 1
            else:
                back = mid - 1

        return front


if __name__ == '__main__':
    # solution = Solution([1, 1, 1, 1, 1])
    # for _ in range(5):
    #     print(solution.pickIndex())
    solution = Solution([1, 2, 3, 4, 5])
    # solution = Solution([1])
    # 1 -> 0
    # 2 -> 1 ~ 2
    # 3 -> 3 ~ 5
    # 4 -> 6 ~ 10
    # 5 -> 11 ~ 15
    # for i in range(1, sum([1, 2, 3, 4, 5]) + 1):
    #     print(solution.pickIndex(i))
    for i in range(15):
        print(solution.pickIndex(i))
