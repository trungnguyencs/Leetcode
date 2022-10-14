# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = fast = slow = ListNode(next=head)
        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        slow.next = slow.next.next
        return dummy.next