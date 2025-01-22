from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        # max heap
        self.low_heap = []
        # min heap
        self.high_heap = []

    def addNum(self, num: int) -> None:
        if not self.low_heap:
            heappush(self.low_heap, -num)
            return

        if len(self.low_heap) > len(self.high_heap):
            heappush(self.high_heap, num)
        else:
            heappush(self.low_heap, -num)

        if -self.low_heap[0] > self.high_heap[0]:
            low = -heappop(self.low_heap)
            high = heappop(self.high_heap)
            heappush(self.low_heap, -high)
            heappush(self.high_heap, low)

    def findMedian(self) -> float:
        if len(self.low_heap) == len(self.high_heap):
            return (-self.low_heap[0] + self.high_heap[0]) / 2
        else:
            return -self.low_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
if __name__ == '__main__':
    median_finder = MedianFinder()
    median_finder.addNum(1)
    print(median_finder.findMedian())
    median_finder.addNum(2)
    print(median_finder.findMedian())
    median_finder.addNum(3)
    print(median_finder.findMedian())
