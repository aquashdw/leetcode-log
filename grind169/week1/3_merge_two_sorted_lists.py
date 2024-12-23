from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2
        if list1.val < list2.val:
            first = list1
            list1 = list1.next
        else:
            first = list2
            list2 = list2.next
        head = first
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        head.next = list1 if list1 else list2
        return first


if __name__ == '__main__':
    # list1 = ListNode(1, ListNode(2, ListNode(4)))
    # list2 = ListNode(1, ListNode(3, ListNode(4)))
    list1 = ListNode(1, None)
    list2 = None

    head = Solution().mergeTwoLists(list1, list2)
    while head:
        print(head.val)
        head = head.next
