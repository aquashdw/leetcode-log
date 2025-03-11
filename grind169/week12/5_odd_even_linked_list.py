from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}, {self.next is not None}'


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd_tail = head
        odd_head = odd_tail
        even_tail = head.next
        even_head = even_tail
        node = head.next.next
        odd = True
        while node:
            if odd:
                odd_tail.next = node
                odd_tail = odd_tail.next
            else:
                even_tail.next = node
                even_tail = even_tail.next

            node = node.next
            odd = not odd

        head = odd_head
        odd_tail.next = even_head
        even_tail.next = None

        return head


def list_to_nodes(vals):
    if not vals:
        return None

    head = ListNode(vals[0])
    node = head
    for idx in range(1, len(vals)):
        node.next = ListNode(vals[idx])
        node = node.next
    return head


if __name__ == '__main__':
    solution = Solution()
    node = solution.oddEvenList(list_to_nodes([1, 2, 3, 4, 5]))
    while node:
        print(node.val, end=' ')
        node = node.next
    print()

    node = solution.oddEvenList(list_to_nodes([2, 1, 3, 5, 6, 4, 7]))
    while node:
        print(node.val, end=' ')
        node = node.next
    print()
