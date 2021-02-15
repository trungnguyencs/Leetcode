# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, K: int) -> ListNode:
        if self.isLengthLessThanK(head, K): return head
        prev, cur = None, head
        for _ in range(K):
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        head.next = self.reverseKGroup(nxt, K)
        return prev
        
    def isLengthLessThanK(self, head, K):
        for _ in range(K):
            if not head: return True
            head = head.next
        return False