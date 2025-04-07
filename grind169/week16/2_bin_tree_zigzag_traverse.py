from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        next_queue = deque([root])
        level = 0
        while next_queue:
            now_queue = next_queue
            next_queue = deque()
            row = []
            while now_queue:
                now = now_queue.popleft()
                row.append(now.val)
                if level % 2:
                    if now.right:
                        next_queue.appendleft(now.right)
                    if now.left:
                        next_queue.appendleft(now.left)
                else:
                    if now.left:
                        next_queue.appendleft(now.left)
                    if now.right:
                        next_queue.appendleft(now.right)

            result.append(row)
            level += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(
        3,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7),
        )
    )
    print(solution.zigzagLevelOrder(root))

    root = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(4)
        ),
        TreeNode(
            3,
            None,
            TreeNode(5)
        )
    )
    print(solution.zigzagLevelOrder(root))
