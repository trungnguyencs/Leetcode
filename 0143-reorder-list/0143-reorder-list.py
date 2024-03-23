# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head 
        head1, head2 = head, self.reverse(self.getMiddle(head))
        cur = dummy = ListNode()
        while head1:
            cur.next = head1
            cur, head1 = cur.next, head1.next
            cur.next = head2
            cur, head2 = cur.next, head2.next
        return dummy.next
        
    def getMiddle(self, head):
        prev = None
        slow = fast = head
        while fast and fast.next:
            slow, fast, prev = slow.next, fast.next.next, slow
        prev.next = None
        return slow
    
    def reverse(self, head):
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        return prev