from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        forehead = ListNode()
        node = forehead
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next

        if left:
            node.next = left
        if right:
            node.next = right

        return forehead.next

    def divide(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = slow.next
        slow.next = None

        left = self.divide(left)
        right = self.divide(right)

        return self.merge(left, right)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.divide(head)


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
    head = list_to_node([4, 2, 1, 3])
    head = solution.sortList(head)
    while head:
        print(head.val)
        head = head.next
