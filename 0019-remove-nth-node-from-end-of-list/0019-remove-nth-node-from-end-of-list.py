# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = cur = ListNode(next=head)
        for _ in range(self.getLen(head) - n):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next
        
    def getLen(self, head):
        count = 0
        while head:
            head = head.next
            count += 1
        return count