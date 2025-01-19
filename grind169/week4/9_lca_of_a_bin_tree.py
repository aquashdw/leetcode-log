# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root

        p_path = []
        q_path = []
        self.find_path(root, p_path, p.val)
        self.find_path(root, q_path, q.val)
        p_len = len(p_path)
        q_len = len(q_path)
        for i in range(1, min(p_len, q_len)):
            if p_path[i].val != q_path[i].val:
                return p_path[i - 1]

        if p_len < q_len:
            return p_path[-1]
        else:
            return q_path[-1]

    def find_path(self, root: TreeNode, path: List[TreeNode], target):
        if root is None:
            return False

        path.append(root)
        if root.val == target or \
                self.find_path(root.left, path, target) or \
                self.find_path(root.right, path, target):
            return True

        path.pop()
        return False
