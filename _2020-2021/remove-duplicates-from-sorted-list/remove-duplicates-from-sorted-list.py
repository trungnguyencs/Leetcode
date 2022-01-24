# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        prev, cur = dummy, head
        while cur:
            if cur.next and cur.val == cur.next.val:
                cur = cur.next
            else:
                prev.next = cur
                prev, cur = cur, cur.next
        return dummy.next
