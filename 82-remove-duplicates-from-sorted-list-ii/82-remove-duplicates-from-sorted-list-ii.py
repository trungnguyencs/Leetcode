# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode('#', head)
        prev, cur = dummy, head
        while cur and cur.next:
            if cur.val == cur.next.val:       
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next # cur is the last duplicated element => need 1 more jump
                prev.next = cur
            else:
                prev, cur = cur, cur.next
        return dummy.next