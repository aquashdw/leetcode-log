# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        pre_len = len(preorder)
        in_len = len(inorder)
        if pre_len == 1 and in_len == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        root_inorder = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:1 + root_inorder], inorder[:root_inorder])
        root.right = self.buildTree(preorder[1 + root_inorder:], inorder[root_inorder + 1:])
        return root


if __name__ == '__main__':
    solution = Solution()
    head = solution.buildTree([1, 2, 3, 4, 5, 6, 7], [3, 2, 4, 1, 6, 5, 7])
    print(head.val)
