# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.diameter = 0
        self.post_traverse(root)
        return self.diameter

    def post_traverse(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.post_traverse(root.left)
        right_depth = self.post_traverse(root.right)
        self.diameter = max(left_depth + right_depth, self.diameter)
        return max(left_depth, right_depth) + 1
