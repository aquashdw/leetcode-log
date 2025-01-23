from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        fast = head
        slow = head
        nodes = 1
        while fast.next:
            fast = fast.next
            nodes += 1
            if nodes % 2 == 0:
                slow = slow.next

        return slow


if __name__ == '__main__':
    solution = Solution()
    print(solution.middleNode(ListNode(1, ListNode(2))).val)
    print(solution.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))).val)
    print(solution.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))).val)
