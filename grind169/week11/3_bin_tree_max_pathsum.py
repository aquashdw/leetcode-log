from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_pathsum = None

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_pathsum = -30000000
        self.post_traverse(root)
        return self.max_pathsum

    def post_traverse(self, root: Optional[TreeNode]) -> Optional[int]:
        if not root:
            return None

        left_pathsum = self.post_traverse(root.left)
        left_pathsum = -30000000 if left_pathsum is None else left_pathsum
        right_pathsum = self.post_traverse(root.right)
        right_pathsum = -30000000 if right_pathsum is None else right_pathsum
        with_now_pathsum = max(left_pathsum, right_pathsum, left_pathsum + right_pathsum, 0) + root.val
        self.max_pathsum = max(left_pathsum, right_pathsum, with_now_pathsum, self.max_pathsum)
        return max(left_pathsum, right_pathsum, 0) + root.val


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPathSum(TreeNode(
        1,
        left=TreeNode(2),
        right=TreeNode(3),
    )))
    print(solution.maxPathSum(TreeNode(-3)))
