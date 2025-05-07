from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        ret_head = None
        last = None
        front = head
        back = head
        diff = 0
        while back:
            if diff == k - 1:
                next_start = back.next
                stack = []
                while front != back:
                    stack.append(front)
                    front = front.next
                front = back
                node = front
                while stack:
                    node.next = stack.pop()
                    node = node.next

                if not ret_head:
                    ret_head = front
                if last:
                    last.next = front
                last = node
                last.next = None
                front = back = next_start
                diff = 0
            if back:
                back = back.next
                diff += 1

        last.next = front

        return ret_head


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))), 2))
