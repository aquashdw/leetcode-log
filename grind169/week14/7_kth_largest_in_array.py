from collections import defaultdict
from typing import List
from heapq import heappush, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        count = defaultdict(int)
        for num in nums:
            if num not in count:
                heappush(heap, -num)
            count[num] += 1

        counted = 0
        while counted + count[-heap[0]] < k:
            counted += count[-heappop(heap)]

        return -heappop(heap)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
