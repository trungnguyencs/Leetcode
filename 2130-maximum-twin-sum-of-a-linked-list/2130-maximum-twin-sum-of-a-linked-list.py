# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        newHead = self.reverse(slow.next)
        slow.next = None
        maxSum = float('-inf')
        while head:
            maxSum = max(maxSum, head.val + newHead.val)
            head = head.next
            newHead = newHead.next
        return maxSum
        
    def reverse(self, head):
        cur, prev = head, None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        return prev