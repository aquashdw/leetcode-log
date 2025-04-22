from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def build_tree(start, end):
            if start == end:
                return TreeNode(nums[start])
            mid = (end + start) // 2
            if mid == start:
                return TreeNode(
                    nums[start],
                    None,
                    TreeNode(nums[end])
                )
            elif mid == end:
                return TreeNode(
                    nums[end],
                    TreeNode(nums[start])
                )
            return TreeNode(
                nums[mid],
                build_tree(start, mid - 1),
                build_tree(mid + 1, end)
            )

        root = build_tree(0, len(nums) - 1)
        return root


if __name__ == '__main__':
    solution = Solution()
    tree = solution.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(tree)
    tree = solution.sortedArrayToBST([1, 3])
    print(tree)
