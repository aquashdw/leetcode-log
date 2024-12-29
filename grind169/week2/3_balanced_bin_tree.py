# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(node_values: List[int]) -> TreeNode:
    tree_nodes = [TreeNode(value) for value in node_values]
    for i in range(len(tree_nodes)):
        root_node = tree_nodes[i]
        if 2 * i + 1 >= len(tree_nodes):
            break
        if 2 * i + 1 < len(tree_nodes) and tree_nodes[2 * i + 1].val is not None:
            root_node.left = tree_nodes[2 * i + 1]
        if 2 * i + 2 < len(tree_nodes) and tree_nodes[2 * i + 1].val is not None:
            root_node.right = tree_nodes[2 * i + 2]
    return tree_nodes[0]


class Solution:
    balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.get_depth(root)
        return self.balanced

    def get_depth(self, root: Optional[TreeNode]):
        if not root:
            return 0
        if not self.balanced:
            return 0
        left_depth = 0
        right_depth = 0
        if root.left:
            left_depth = self.get_depth(root.left)
        if root.right:
            right_depth = self.get_depth(root.right)

        if abs(left_depth - right_depth) > 1:
            self.balanced = False
            return 0

        depth = max(left_depth, right_depth) + 1
        return depth


if __name__ == '__main__':
    null = None
    testcase = [-77, 24, -48, -74, 43, -27, -14, 84, 6, 51, 36, -90, -18, -84, -6, 93, 83, 95, -94, 75, -19, -98, 15,
                -54, 72, 78, 2, -56, null, 12, -47, null, 28, null, null, 58, 13, -31, -39, 33, null, null, -96, null,
                29, -95, -53, null, null, -50, null, 54, 99, 8, null, null, null, -45, 42, -46, null, null, null, 59,
                66, -93, -11, -62, -9, 79, 57, -34, 64, null, null, null, -72, null, -40, 90, null, -49, null, 35, -38,
                44, -12, null, null, null, null, null, null, null, null, null, null, null, 22, null, -63, -32, -100,
                null, -89, -8, 27, 19, 34, 81, 45, null, 92, -21, null, 61, 50, null, -43, null, -15, null, null, null,
                null, null, null, -67, 53, -41, null, -3, -85, 91, 26, -16, null, null, null, 49, null, 87, -33, 23,
                -58, null, 30, null, null, -10, -86, null, null, 47, 16, null, -2, null, null, null, null, null, null,
                null, null, null, null, null, null, null, null, -66, -68, null, 17, 82, null, null, null, null, null,
                null, null, null, null, -81, 37, 38, -36, -24, 18, null, 65, 94, -51, 63, null, -78, 77, -4, 60, 1,
                null, null, null, -22, null, 32, -60, null, 21, 80, 52, null, -57, -28, 11, null, null, 89, 41, -87,
                null, 25, -75, 48, -35, -61, -13, null, 71, 85, -29, null, null, 10, null, null, null, null, -91, 3,
                null, 9, null, null, null, null, null, 0, -7, 67, null, null, null, 7, -82, -55, null, 56, 73, null,
                null, -70, 4, -71, 98, 55, null, null, null, 5, 40, null, null, null, null, -97, null, null, -26, -92,
                68, null, null, 86, null, -80, null, -88, null, 69, null, null, null, -5, 31, null, null, -42, null,
                null, null, null, null, null, null, null, null, -64, null, -76, 62, 39, -17, null, null, -23, -44, null,
                null, null, null, 97, null, -83, -59, null, null, null, 46, -79, null, -99, null, null, null, -65, null,
                -30, null, null, null, 20, -52, null, -1, null, -69, -25, 88, -20, null, null, null, null, null, null,
                null, null, null, 74, 96, 76, -37, null, null, null, 14, null, null, null, null, null, null, null, null,
                null, null, null, null, -73, 70]
    # print(len(testcase))
    #
    # idx = 0
    # while idx < 5010:
    #     print(f"{idx}: {testcase[idx]}")
    #     idx = idx * 2 + 1

    solution = Solution()

    root = list_to_tree([3, 9, 20, None, None, 15, 7])
    print(solution.isBalanced(root))

    root = list_to_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    print(solution.isBalanced(root))

    root = list_to_tree(testcase)
    print(solution.isBalanced(root))
