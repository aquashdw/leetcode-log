from collections import deque
from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        node_map = {
            1: Node(1)
        }
        to_visit = deque()
        to_visit.append(node)
        while to_visit:
            next_node = to_visit.popleft()
            new_node = node_map[next_node.val]
            for neighbor in next_node.neighbors:
                if neighbor.val not in node_map.keys():
                    node_map[neighbor.val] = Node(neighbor.val)
                    to_visit.append(neighbor)
                new_node.neighbors.append(node_map[neighbor.val])
        return node_map[1]
