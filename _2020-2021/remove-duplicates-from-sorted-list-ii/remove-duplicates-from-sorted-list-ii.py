# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode(next=head)
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                # now cur is at the last repeated digit, need 1 more jump
                cur = cur.next
                prev.next = cur
            else:
                prev, cur = prev.next, cur.next
        return dummy.next