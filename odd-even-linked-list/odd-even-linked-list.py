# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        oddHead = odd = head
        evenHead = even = head.next
        while odd.next and odd.next.next:
            odd.next = even.next
            even.next = odd.next.next
            odd = odd.next
            even = even.next
        odd.next = evenHead
        return head