from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        red = 0
        while red < n and nums[red] == 0:
            red += 1
        if red == n:
            # all red
            return
        blue = n - 1
        while blue > 0 and nums[blue] == 2:
            blue -= 1
        if blue == -1:
            # all blue
            return
        now = red
        while now <= blue:
            if nums[now] == 2:
                nums[now], nums[blue] = nums[blue], nums[now]
                while red <= blue and nums[blue] == 2:
                    blue -= 1

            if nums[now] == 0 and now != red:
                nums[now], nums[red] = nums[red], nums[now]
            while red <= blue and nums[red] == 0:
                red += 1

            now = max(red, now + 1)

        return


if __name__ == '__main__':
    solution = Solution()
    # in_list = [2, 0, 2, 1, 1, 0]
    # in_list = [2, 0, 1]
    in_list = [0, 0, 2, 1, 1, 2, 1, 1, 1, 0, 2, 1, 0, 1, 2, 1, 0, 1, 1, 1, 2, 2, 1, 2, 0, 0, 1, 0, 2, 1, 2, 2, 2, 0]
    solution.sortColors(in_list)
    print(in_list)
