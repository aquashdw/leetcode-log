from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
                continue

            if asteroid * stack[-1] > 0:
                stack.append(asteroid)
                continue

            if stack[-1] < 0 < asteroid:
                stack.append(asteroid)
                continue

            stack.append(asteroid)
            while len(stack) > 1:
                right = stack.pop()
                left = stack.pop()
                if right * left > 0:
                    stack.append(left)
                    stack.append(right)
                    break
                r_size = abs(right)
                l_size = abs(left)
                if r_size == l_size:
                    break
                elif r_size > l_size:
                    stack.append(right)
                else:
                    stack.append(left)
                    break

        return stack


if __name__ == '__main__':
    solution = Solution()
    print(solution.asteroidCollision([5, 10, -5]))
    print(solution.asteroidCollision([8, -8]))
    print(solution.asteroidCollision([10, 2, -5]))
    print(solution.asteroidCollision([-2, -1, 1, 2]))
    print(solution.asteroidCollision([-2, -2, 1, -2]))
