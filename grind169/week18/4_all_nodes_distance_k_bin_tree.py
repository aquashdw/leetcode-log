from collections import deque, defaultdict
from typing import List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}"


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj_list = {}

        queue = deque()
        queue.append(root)
        target_node = None
        while queue:
            now = queue.popleft()
            if now.val == target.val:
                target_node = now
                break

            if now.left:
                adj_list[now.left.val] = now
                queue.append(now.left)
            if now.right:
                adj_list[now.right.val] = now
                queue.append(now.right)

        if k == 0:
            return [target_node.val]

        result = []
        queue.clear()
        queue.append((target_node, 0))
        visited = set()
        visited.add(target_node.val)
        while queue:
            now, dist = queue.popleft()
            if dist + 1 == k:
                if now.left and now.left.val not in visited:
                    result.append(now.left.val)
                if now.right and now.right.val not in visited:
                    result.append(now.right.val)
                if now.val in adj_list and adj_list[now.val].val not in visited:
                    result.append(adj_list[now.val].val)
                continue
            if now.left and now.left.val not in visited:
                visited.add(now.left.val)
                queue.append((now.left, dist + 1))
            if now.right and now.right.val not in visited:
                visited.add(now.right.val)
                queue.append((now.right, dist + 1))
            if now.val in adj_list and adj_list[now.val].val not in visited:
                visited.add(adj_list[now.val].val)
                queue.append((adj_list[now.val], dist + 1))

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.distanceK(
        TreeNode(
            0,
            TreeNode(
                1,
                TreeNode(
                    2,
                    TreeNode(7),
                    TreeNode(4, None, TreeNode(5))
                ),
                TreeNode(3)
            ),
            TreeNode(6)
        ),
        TreeNode(1),
        3
    ))
