BAD_VERSION = 4


def set_bad_version(version: int):
    global BAD_VERSION
    BAD_VERSION = version


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= BAD_VERSION


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    solution = Solution()

    set_bad_version(7)
    print(solution.firstBadVersion(10))
