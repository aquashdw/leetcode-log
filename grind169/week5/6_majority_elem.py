from typing import List


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     count = defaultdict(lambda: 0)
    #     for num in nums:
    #         count[num] += 1
    #
    #     major = nums[0]
    #     major_val = count[nums[0]]
    #     for num in count:
    #         if count[num] > major_val:
    #             major = num
    #             major_val = count[num]
    #     return major
    def majorityElement(self, nums: List[int]) -> int:
        major = None
        count = 0
        for num in nums:
            if count == 0:
                major = num
            if major == num:
                count += 1
            else:
                count -= 1
        return major


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([2, 1, 2]))
