from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{}".format(self.val)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # single node list
        if not head.next:
            return None

        # last node removal
        if n == 1:
            if not head.next:
                return None

            pointer = head
            before = None
            while pointer.next:
                before = pointer
                pointer = pointer.next

            before.next = None
            return head

        fast = head
        slow = head

        idx = 0
        record = []
        while idx < n:
            if not (fast and fast.next):
                break

            fast = fast.next.next
            record.append(slow)
            slow = slow.next
            idx += 1

        if idx == n:
            before = record.pop()
            while fast:
                fast = fast.next
                before = slow
                slow = slow.next

            before.next = slow.next
            return head

        offset = n - idx - (1 if fast else 0)
        if offset == 0:
            record.pop().next = slow.next
            return head

        target = record.pop()
        for i in range(offset - 1):
            target = record.pop()
        if not record:
            return target.next

        record.pop().next = target.next

        return head


def list_to_node(vals):
    if not vals:
        return None

    head = ListNode(vals[0])
    node = head
    for i in range(1, len(vals)):
        node.next = ListNode(vals[i])
        node = node.next

    return head


if __name__ == '__main__':
    solution = Solution()
    solution.removeNthFromEnd(list_to_node([0, 1]), 2)
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5]), 4)
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6]), 5)
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6]), 6)
    # # True 4 2 -> go to back
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5]), 2)
    # # True None 3 -> 3 Done
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5]), 3)
    # # False None 3 -> 2
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5]), 4)
    # # True 4 2 -> go to back Done
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6]), 2)
    # # True 6 3 -> 4 Done
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6]), 3)
    # # False 6 3 -> 3
    solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6]), 4)
    # # True 4 2 -> go to back Done
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6, 7]), 2)
    # # True 6 3 -> go to back Done
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6, 7]), 3)
    # # True None 4 -> 4 Done
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6, 7]), 4)
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6, 7]), 5)
