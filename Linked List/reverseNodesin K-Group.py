# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth_node = self.getCount(group_prev, k)
            if not kth_node:
                break 

            group_start = group_prev.next
            group_end = kth_node
            next_group = group_end.next

            group_end.next = None

            new_group_start = self.reverseList(group_start)

            group_prev.next = new_group_start
            group_start.next = next_group

            group_prev = group_start

        return dummy.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

    def getCount(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if not curr.next:
                return None
            curr = curr.next
        return curr
