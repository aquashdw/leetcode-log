# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    # BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        depth = 1
        queue.append((root, 1))
        while queue:
            node, node_depth = queue.popleft()
            depth = max(depth, node_depth)

            if node.left:
                queue.append((node.left, node_depth + 1))
            if node.right:
                queue.append((node.right, node_depth + 1))

        return depth
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def get_depth(node):
            if not node:
                return 0
            return 1 + max(get_depth(node.left), get_depth(node.right))

        return get_depth(root)
