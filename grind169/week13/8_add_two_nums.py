from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        forehead = ListNode()
        node = forehead
        over = 0
        while l1 or l2:
            new_node = ListNode()
            val = l1.val if l1 else 0
            val += l2.val if l2 else 0
            val += over
            over = val // 10
            val %= 10
            new_node.val = val
            node.next = new_node
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if over:
            node.next = ListNode(1)

        return forehead.next


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
    node = solution.addTwoNumbers(list_to_node([2, 4, 3]), list_to_node([5, 6, 4]))
    while node:
        print(node.val, end=' ')
        node = node.next
    print()
    node = solution.addTwoNumbers(list_to_node([9, 9, 9, 9, 9, 9, 9]), list_to_node([9999]))
    while node:
        print(node.val, end=' ')
        node = node.next
    print()
