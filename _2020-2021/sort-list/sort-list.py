# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        fast = slow = head
        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        head2 = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(head2))
    
    def merge(self, head1, head2):
        dummy = cur = ListNode()
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        cur.next = head1 or head2
        return dummy.next