from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        new_interval = newInterval
        new_intervals = []
        for interval in intervals:
            if interval[1] < new_interval[0]:
                new_intervals.append(interval)
            elif new_interval[1] < interval[0]:
                new_intervals.append(new_interval)
                new_interval = interval
            else:
                new_interval[0] = min(interval[0], new_interval[0])
                new_interval[1] = max(interval[1], new_interval[1])
        new_intervals.append(new_interval)
        return new_intervals


if __name__ == '__main__':
    solution = Solution()
    print(solution.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
    print(solution.insert(intervals=[[1, 5]], newInterval=[2, 3]))
    print(solution.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
    print(solution.insert(intervals=[[1, 2], [5, 7], [8, 10], [12, 16]], newInterval=[4, 6]))
    print(solution.insert(intervals=[[1, 2], [5, 7], [8, 10], [12, 16]], newInterval=[3, 4]))
    print(solution.insert(intervals=[[5, 7], [8, 10]], newInterval=[3, 4]))
    print(solution.insert(intervals=[[5, 7], [8, 10]], newInterval=[11, 15]))
    print(solution.insert(intervals=[[5, 7], [11, 15]], newInterval=[8, 10]))
