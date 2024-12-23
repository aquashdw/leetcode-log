from typing import List


class SolutionBF:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for idx, num in enumerate(nums):
            if target - num in record.keys():
                return [record[target - num], idx]
            else:
                record[num] = idx
        return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for idx, num in enumerate(nums):
            if target - num in record.keys():
                return [record[target - num], idx]
            else:
                record[num] = idx
        return []


if __name__ == '__main__':
    print(Solution().twoSum(nums=[3, 2, 4], target=6))
