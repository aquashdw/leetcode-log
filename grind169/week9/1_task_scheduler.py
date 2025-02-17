from heapq import heappush, heappop
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        def atoi(char):
            return ord(char) - ord('A')

        def push(item):
            heappush(task_heap, item)

        def pop():
            return heappop(task_heap)

        def peek():
            return task_heap[0]

        task_heap = []
        tasks_left = [0 for _ in range(26)]
        max_task = atoi(tasks[0])
        for task in tasks:
            tasks_left[atoi(task)] += 1
            max_task = atoi(task) if tasks_left[atoi(task)] > tasks_left[max_task] else max_task

        for task, count in enumerate(tasks_left):
            if count == 0:
                continue
            push((-count, task))

        next_clock = [0 for _ in range(26)]
        clock = 0
        while task_heap:
            temp_heap = []
            while task_heap and clock < next_clock[peek()[1]]:
                heappush(temp_heap, pop())

            if not task_heap:
                task_heap = temp_heap
            else:
                count, task = pop()
                if -count > 1:
                    push((count + 1, task))
                    next_clock[task] += n + 1

                while temp_heap:
                    push(heappop(temp_heap))
            clock += 1

        return clock


if __name__ == '__main__':
    solution = Solution()
    print(solution.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
    print(solution.leastInterval(["A", "C", "D", "B", "D", "B"], 1))
    print(solution.leastInterval(["A", "A", "A", "B", "B", "B"], 3))
    print(solution.leastInterval(["B", "C", "D", "A", "A", "A", "A", "G"], 1))
