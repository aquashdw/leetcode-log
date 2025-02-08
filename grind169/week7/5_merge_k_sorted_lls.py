from typing import List, Optional
from heapq import heappush, heappop


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'val: {self.val}, has_next: {self.next is not None}'


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        heap = []
        next_idx = 0

        def push(node, heap_idx):
            heappush(heap, (node.val, heap_idx, node))

        def pop():
            return heappop(heap)[2]

        for head in lists:
            if not head:
                continue
            push(head, next_idx)
            next_idx += 1

        if not heap:
            return

        head = pop()
        if head.next:
            push(head.next, next_idx)
            next_idx += 1

        now = head
        while heap:
            popped = pop()
            if popped.next:
                push(popped.next, next_idx)
                next_idx += 1
            now.next = popped
            now = now.next

        return head


if __name__ == '__main__':
    solution = Solution()
    result = solution.mergeKLists([
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6)),
    ])
    while result:
        print(result.val)
        result = result.next

    result = solution.mergeKLists([ListNode(1)])
