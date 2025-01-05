# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        next_visit = deque()
        next_visit.append(root)
        now_visit = deque()
        result = []
        while next_visit:
            now_visit, next_visit = next_visit, now_visit
            visited = []
            while now_visit:
                now = now_visit.popleft()
                visited.append(now.val)
                if now.left:
                    next_visit.append(now.left)
                if now.right:
                    next_visit.append(now.right)
            result.append(visited)
        return result
