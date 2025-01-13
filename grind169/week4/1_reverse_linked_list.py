# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail = head
        next = head.next
        tail.next = None
        while next:
            temp = next.next
            next.next = tail
            tail = next
            if not temp:
                return next
            next = temp
