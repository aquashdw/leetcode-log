from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        back = head.next
        if not back:
            return head

        back.next, head.next = head, back.next
        if not head.next:
            return back

        before = head
        front = head.next
        head = back
        back = front.next
        while front and back:
            next_front = back.next
            before.next = back
            back.next = front
            front.next = next_front
            before = front
            front = next_front
            if front:
                back = front.next

        return head


if __name__ == '__main__':
    solution = Solution()
    node = solution.swapPairs(ListNode(1, ListNode(2)))
    while node:
        print(node.val, end=' ')
        node = node.next
    print()
    node = solution.swapPairs(ListNode(1, ListNode(2, ListNode(3))))
    while node:
        print(node.val, end=' ')
        node = node.next
    print()
    node = solution.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    while node:
        print(node.val, end=' ')
        node = node.next
    print()
    node = solution.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    while node:
        print(node.val, end=' ')
        node = node.next
    print()
    node = solution.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    while node:
        print(node.val, end=' ')
        node = node.next
    print()
