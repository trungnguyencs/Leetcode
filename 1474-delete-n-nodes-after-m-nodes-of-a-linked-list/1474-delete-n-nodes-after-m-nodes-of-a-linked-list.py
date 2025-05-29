# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        cur = dummy = ListNode(next=head)
        keep = delete = 0
        while cur and keep < m:
            cur = cur.next
            keep += 1
        while cur and cur.next and delete < n:
            cur.next = cur.next.next
            delete += 1
        if cur and cur.next:
            self.deleteNodes(cur.next, m, n)
        return dummy.next