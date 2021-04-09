# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head
        # detach 1st half and 2nd half
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None
        # reverse 2nd half
        head2 = self.reverse(slow)
        # combine 1st half and 2nd half
        cur = dummy = ListNode()
        while head:
            cur.next = head
            cur, head = cur.next, head.next
            cur.next = head2
            cur, head2 = cur.next, head2.next
        cur.next = head or head2
        return dummy.next
    
    def reverse(self, head):
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        return prev