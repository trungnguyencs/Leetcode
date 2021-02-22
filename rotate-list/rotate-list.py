# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length, tail = self.getLengthAndTail(head)
        if length == 0 or k % length == 0: return head
        k %= length
        cur = head
        for _ in range(length - k - 1): # have to stop 1 element earlier
            cur = cur.next
        newHead, cur.next, tail.next = cur.next, None, head
        return newHead
        
    def getLengthAndTail(self, head):
        prev, length = None, 0
        while head:
            prev, head = head, head.next
            length += 1
        return length, prev