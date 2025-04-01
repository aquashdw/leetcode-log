from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        de_queue = deque()
        while head:
            de_queue.append(head.val)
            head = head.next

        while len(de_queue) > 1:
            if de_queue[0] != de_queue[-1]:
                return False
            de_queue.pop()
            de_queue.popleft()

        return True
