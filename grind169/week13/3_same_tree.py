from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse_both(self, a_node: Optional[TreeNode], b_node):
        if (a_node and not b_node) or (not a_node and b_node):
            return False
        # both are leaf
        if not a_node and not b_node:
            return True

        # val are different
        if a_node.val != b_node.val:
            return False
        # check left
        if not self.traverse_both(a_node.left, b_node.left):
            return False
        # check right
        return self.traverse_both(a_node.right, b_node.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traverse_both(p, q)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))))
