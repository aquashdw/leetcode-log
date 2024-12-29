# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_nodes(node_values: List[int], pos: int):
    nodes = [ListNode(value) for value in node_values]
    for i in range(len(nodes) - 1):
        front = nodes[i]
        back = nodes[i + 1]
        front.next = back

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


class Solution:
    """
    first try: set with ids
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ids = set()
        while head:
            head_id = id(head)
            if head_id in ids:
                return True
            ids.add(head_id)
            head = head.next
        return False
    """

    # Floyd's cycle detection
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()

    node = list_to_nodes([3, 2, 0, -4], 1)
    print(solution.hasCycle(node))
