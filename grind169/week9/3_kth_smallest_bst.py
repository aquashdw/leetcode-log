from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        head = root
        stack = [head]
        while head.left:
            stack.append(head.left)
            head = head.left

        for _ in range(k - 1):
            head = stack.pop()
            head = head.right
            while head:
                stack.append(head)
                head = head.left

        return stack[-1].val


if __name__ == '__main__':
    solution = Solution()
    print(solution.kthSmallest(
        root=TreeNode(
            3,
            left=TreeNode(
                1,
                left=None,
                right=TreeNode(2),
            ),
            right=TreeNode(
                4,
            )
        ),
        k=1
    ))

    print(solution.kthSmallest(
        TreeNode(
            5,
            left=TreeNode(
                3,
                left=TreeNode(
                    2,
                    left=TreeNode(
                        1,
                    )
                ),
                right=TreeNode(
                    4,
                ),
            ),
            right=TreeNode(6)
        ),
        3
    ))
