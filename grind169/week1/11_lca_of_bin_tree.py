# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root
        if p.val > q.val:
            p, q = q, p

        while not p.val <= ancestor.val <= q.val:
            if p.val >= ancestor.val:
                ancestor = ancestor.right
            elif q.val <= ancestor.val:
                ancestor = ancestor.left

        return ancestor


def list_to_tree(node_values: List[int]) -> TreeNode:
    tree_nodes = [TreeNode(value) for value in node_values]
    for i in range(len(tree_nodes)):
        root_node = tree_nodes[i]
        if 2 * i + 1 >= len(tree_nodes):
            break
        if 2 * i + 1 < len(tree_nodes):
            root_node.left = tree_nodes[2 * i + 1]
        if 2 * i + 2 < len(tree_nodes):
            root_node.right = tree_nodes[2 * i + 2]
    return tree_nodes[0]


if __name__ == '__main__':
    solution = Solution()

    root = list_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(solution.lowestCommonAncestor(root, TreeNode(2), TreeNode(8)).val)
    print(solution.lowestCommonAncestor(root, TreeNode(3), TreeNode(4)).val)

    root = list_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(solution.lowestCommonAncestor(root, TreeNode(2), TreeNode(4)).val)

    root = list_to_tree([2, 1])
    print(solution.lowestCommonAncestor(root, TreeNode(2), TreeNode(1)).val)
