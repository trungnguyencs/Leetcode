# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'))
        while head:
            prev, nxt = dummy, head.next
            head.next = None
            while prev.next and prev.next.val < head.val:
                prev = prev.next
            prev.next, head.next = head, prev.next
            head = nxt
        return dummy.next