from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []
        for idx, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                lower = stack.pop()
                result[lower] = idx - lower
            stack.append(idx)

        return result
