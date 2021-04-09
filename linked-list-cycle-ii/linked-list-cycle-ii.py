# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next: 
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                while not head is slow:
                    head, slow = head.next, slow.next
                return head 
        return None