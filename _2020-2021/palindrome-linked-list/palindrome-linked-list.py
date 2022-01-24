# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        middle = self.findMiddle(head)
        head2 = self.reverse(middle.next)
        middle.next = None
        while head: #len(list2) is greater than len(list1) by at most 1
            if head.val != head2.val:
                return False
            head, head2 = head.next, head2.next
        return True
        
    def findMiddle(self, head):
        fast = slow = head
        prev = None
        while fast and fast.next:
            slow, fast, prev = slow.next, fast.next.next, slow
        return prev
    
    def reverse(self, head):
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        return prev