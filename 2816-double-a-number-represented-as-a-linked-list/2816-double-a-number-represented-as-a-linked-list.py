# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = self.reverse(head)
        newHead = None
        carry = 0
        while cur or carry:
            if cur:
                carry += cur.val * 2
                cur = cur.next
            newHead = ListNode(carry % 10, next=newHead)
            carry //= 10
        return newHead
    
    def reverse(self, head):
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        return prev