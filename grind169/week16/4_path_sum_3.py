from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        total = 0
        # this keeps track of previous sums in path
        count_dict = defaultdict(int)
        count_dict[0] = 1

        def find(node, current_sum):
            nonlocal total
            current_sum += node.val
            # if there were a previous sum (that can be subtracted)
            # then the target sum can be made
            total += count_dict[current_sum - targetSum]
            count_dict[current_sum] += 1
            if node.left:
                find(node.left, current_sum)
            if node.right:
                find(node.right, current_sum)
            count_dict[current_sum] -= 1

        find(root, 0)
        return total


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(
        10,
        TreeNode(
            5,
            TreeNode(
                3,
                TreeNode(3),
                TreeNode(-2),
            ),
            TreeNode(
                2,
                None,
                TreeNode(1),
            ),
        ),
        TreeNode(
            -3,
            None,
            TreeNode(11)
        ),
    )
    print(solution.pathSum(root, 8))

    root = TreeNode(
        1,
        None,
        TreeNode(
            2,
            None,
            TreeNode(
                3,
                None,
                TreeNode(
                    4,
                    None,
                    TreeNode(5)
                )
            )
        )
    )
    print(solution.pathSum(root, 3))
