from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next

        k %= len(stack)
        if k == 0:
            return head

        new_head = stack[-k]
        stack[-(k + 1)].next = None
        stack[-1].next = head
        return new_head


if __name__ == '__main__':
    solution = Solution()
    head = solution.rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" - ".join(result))
