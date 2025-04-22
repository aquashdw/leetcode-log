from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(origin, target):
            if not origin and not target:
                return True
            if not origin or not target:
                return False
            if origin.val != target.val:
                return False

            return compare(origin.left, target.left) and compare(origin.right, target.right)

        if compare(root, subRoot):
            return True

        def is_subtree(origin, target):
            if not origin:
                return False
            return compare(origin, target) or is_subtree(origin.left, target) or is_subtree(origin.right, target)

        return is_subtree(root, subRoot)
