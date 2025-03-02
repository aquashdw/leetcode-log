from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{}".format(self.val)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # single node list
        if not head.next:
            return None

        fast = head
        slow = head

        idx = 0
        stack = []
        # 우선 n번 이동을 시도한다.
        while idx < n:
            # 만약 토끼가 제일 뒤이거나(fast.next is None)
            # 뒤를 지나치게(fast is None) 되었으면 중단한다.
            if not (fast and fast.next):
                break

            # 그게 아니라면 이동한다.
            fast = fast.next.next
            # 느린 포인터의 노드는 되돌아가기 위해 저장을 먼저 하고,
            stack.append(slow)
            # 돌아간다.
            slow = slow.next
            idx += 1

        # 만약 n번 이동하는데 성공했다면,
        if idx == n:
            # 우선 제일 마지막에 방문한 노드를 꺼내온다.
            # 이는 후에 노드가 제거될 때 연결할 앞의 노드를 가르키는 포인터이다.
            before = stack.pop()
            # 빠른 포인터를
            while fast:
                # 속도를 늦춰서 끝까지 간다.
                fast = fast.next
                # 느린 포인터를 이전 포인터로 지정하고,
                before = slow
                # 느린 포인터도 이동한다.
                slow = slow.next

            # 이제 느린 포인터가 가르키는 노드를 제거한다.
            before.next = slow.next
            return head

        # n번 이동하기 전 빠른 포인터가 끝에 도달할 경우, 얼마나 앞으로 돌아갈지를 결정한다.
        # 이 때 빠른 포인터가
        # 1. 마지막 노드면 (idx)번째 노드는 뒤에서 (idx+1)번째 노드이고, (마지막 노드가 1번째 이기 때문)
        # 2. 마지막 노드 다음(None)이면 (idx)번째 노드는 뒤에서 (idx)번째 노드이다.
        # 이를 고려하여 offset을 결정한다. (빠른 포인터가 None이 아니면 한칸 덜가도 된다)
        offset = n - idx - (1 if fast else 0)
        # 만약 움직일 필요 없다면, (노드의 갯수(count)가 홀수일 때 n == count // 2 + 1일때 발생한다.)
        if offset == 0:
            # 직전 노드의 다음 노드를,
            # 느린 포인터의 다음 노드로 설정한다.
            stack.pop().next = slow.next
            return head

        # 일단 직전 노드를 꺼낸다.
        target = stack.pop()
        # 그리고 offset - 1 만큼 반복해서 앞의 노드를 꺼낸다.
        # 만약 offset이 0이라면 실행되지 않는다.
        for i in range(offset - 1):
            target = stack.pop()
        # 만약 stack이 비어있다면
        if not stack:
            # target이 첫번째 노드가 되고 제거하면 된다.
            return target.next

        # 아니라면 target 노드를 지워준다.
        stack.pop().next = target.next

        return head

    """
    # stack to go back
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # single node list
        if not head.next:
            return None

        # last node removal
        if n == 1:
            if not head.next:
                return None

            pointer = head
            before = None
            while pointer.next:
                before = pointer
                pointer = pointer.next

            before.next = None
            return head

        stack = []
        now = head
        while now:
            stack.append(now)
            now = now.next

        for i in range(n):
            now = stack.pop()

        if not stack:
            return now.next

        front = stack.pop()
        front.back = now.back

        return head
    """


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
    solution.removeNthFromEnd(list_to_node([0, 1]), 2)
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5]), 4)
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6]), 5)
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6]), 6)
    # # True 4 2 -> go to back
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5]), 2)
    # # True None 3 -> 3 Done
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5]), 3)
    # # False None 3 -> 2
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5]), 4)
    # # True 4 2 -> go to back Done
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6]), 2)
    # # True 6 3 -> 4 Done
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6]), 3)
    # # False 6 3 -> 3
    solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6]), 4)
    # # True 4 2 -> go to back Done
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6, 7]), 2)
    # # True 6 3 -> go to back Done
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6, 7]), 3)
    # # True None 4 -> 4 Done
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6, 7]), 4)
    # solution.removeNthFromEnd(list_to_node([0, 1, 2, 3, 4, 5, 6, 7]), 5)
