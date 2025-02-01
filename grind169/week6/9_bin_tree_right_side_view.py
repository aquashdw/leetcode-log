# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        queue = deque()
        queue.append((root, 0))
        while queue:
            now, depth = queue.popleft()
            if len(result) == depth:
                result.append(now.val)
            else:
                result[depth] = now.val

            if now.left:
                queue.append((now.left, depth + 1))
            if now.right:
                queue.append((now.right, depth + 1))

        return result
