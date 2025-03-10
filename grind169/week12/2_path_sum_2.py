from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.paths = []
        self.target_sum = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.paths = []
        self.target_sum = targetSum
        self.dfs(root, 0, [])
        return self.paths

    def dfs(self, node, current_sum, current_path):
        next_sum = current_sum + node.val
        if not node.left and not node.right:
            if next_sum == self.target_sum:
                current_path.append(node.val)
                self.paths.append(current_path.copy())
                current_path.pop()
            return

        current_path.append(node.val)
        if node.left:
            self.dfs(node.left, next_sum, current_path)

        if node.right:
            self.dfs(node.right, next_sum, current_path)
        current_path.pop()


if __name__ == '__main__':
    solution = Solution()
    print(solution.pathSum(TreeNode(-2, right=TreeNode(-3)), -5))
