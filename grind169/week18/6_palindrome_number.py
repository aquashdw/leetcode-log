class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x == 0:
        #     return True
        # if x % 10 == 0 or x < 0:
        #     return False
        #
        # nums = []
        # while x:
        #     nums.append(x % 10)
        #     x //= 10
        # n = len(nums)
        # for i in range(n // 2):
        #     if nums[i] != nums[n - i - 1]:
        #         return False
        #
        # return True
        str_num = str(x)
        return str_num == str_num[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))
