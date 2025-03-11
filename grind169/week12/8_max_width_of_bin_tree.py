from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.lefts = []
        self.rights = []

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.lefts.clear()
        self.rights.clear()
        queue = deque()
        queue.append((root, 0, 0))
        while queue:
            node, depth, idx = queue.popleft()
            if len(self.lefts) == depth:
                self.lefts.append(idx)
            else:
                self.lefts[depth] = min(self.lefts[depth], idx)

            if len(self.rights) == depth:
                self.rights.append(idx)
            else:
                self.rights[depth] = max(self.rights[depth], idx)

            if node.left:
                queue.append((node.left, depth + 1, idx * 2))
            if node.right:
                queue.append((node.right, depth + 1, idx * 2 + 1))

        return max([self.rights[i] - self.lefts[i] for i in range(len(self.lefts))]) + 1
