from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    # simple
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        queue = deque()
        node = head.next
        while node:
            queue.append(node)
            node = node.next

        popleft = False
        node = head
        while queue:
            node.next = queue.popleft() if popleft else queue.pop()
            popleft = not popleft
            node = node.next
        node.next = None
    """

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow

        prev = None
        f_head = mid

        while f_head:
            temp = f_head.next
            f_head.next = prev
            prev = f_head
            f_head = temp

        f_head = head
        b_head = prev

        while f_head and b_head:
            f_head.next, f_head = b_head, f_head.next
            b_head.next, b_head = f_head, b_head.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    solution.reorderList(head)
    while head:
        print(head.val, end=' ')
        head = head.next
