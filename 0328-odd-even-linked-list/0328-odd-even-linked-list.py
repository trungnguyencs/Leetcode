# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = oddHead = ListNode()
        even = evenHead = ListNode()
        while head:
            odd.next = head
            odd, head = odd.next, head.next
            if not head: break
            even.next = head
            even, head = even.next, head.next
        odd.next, even.next = evenHead.next, None
        return oddHead.next