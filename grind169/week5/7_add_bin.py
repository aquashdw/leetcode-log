class Solution:
    def addBinary(self, a: str, b: str) -> str:
        overflow = False
        if len(a) < len(b):
            a, b = b, a
        a_idx = len(a) - 1
        b_idx = len(b) - 1
        result = []
        while b_idx > -1:
            if a[a_idx] == b[b_idx]:
                if a[a_idx] == '1':
                    result.append('1' if overflow else '0')
                    overflow = True
                else:
                    result.append('1' if overflow else '0')
                    overflow = False
            else:
                result.append('0' if overflow else '1')
            a_idx -= 1
            b_idx -= 1

        while a_idx > -1 and overflow:
            if a[a_idx] == '1':
                result.append('0')
            else:
                result.append('1')
                overflow = False
            a_idx -= 1

        while a_idx > -1:
            result.append(a[a_idx])
            a_idx -= 1

        if overflow:
            result.append('1')

        return ''.join(reversed(result))


if __name__ == '__main__':
    solution = Solution()
    # solution.addBinary("11", "1")
    print(solution.addBinary("1010", "1011"))
    print(solution.addBinary("100000", "1"))
    print(solution.addBinary("111111", "1"))
    print(solution.addBinary("101111", "1"))
