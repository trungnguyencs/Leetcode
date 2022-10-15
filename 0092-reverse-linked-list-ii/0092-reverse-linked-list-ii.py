# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = cur = ListNode(next=head)
        for _ in range(left - 1):
            cur = cur.next
        cur.next = self.reverseK(cur.next, right - left + 1)
        return dummy.next
        
    def reverseK(self, head, k):
        prev, cur = None, head
        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        head.next = nxt
        return prev