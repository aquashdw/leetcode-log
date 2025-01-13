# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.is_valid_recursive(root)

    def is_valid_recursive(
            self,
            sub_root: Optional[TreeNode],
            left_bound: int = -(2 ** 31 + 1),
            right_bound: int = 2 ** 31,
    ) -> bool:
        if not sub_root:
            return True
        left = sub_root.left
        if left and not left_bound < left.val < sub_root.val:
            return False
        if not self.is_valid_recursive(left, left_bound=left_bound, right_bound=sub_root.val):
            return False

        right = sub_root.right
        if right and not sub_root.val < right.val < right_bound:
            return False
        if not self.is_valid_recursive(right, left_bound=sub_root.val, right_bound=right_bound):
            return False

        return True
