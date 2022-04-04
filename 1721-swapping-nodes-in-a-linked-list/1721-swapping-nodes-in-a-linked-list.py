# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = dummy = ListNode(next=head)
        for _ in range(k - 1):
            fast = fast.next
        prevLeft, left = fast, fast.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next
        prevRight, right = slow, slow.next
        prevLeft.next, prevRight.next = right, left
        right.next, left.next = left.next, right.next
        return dummy.next