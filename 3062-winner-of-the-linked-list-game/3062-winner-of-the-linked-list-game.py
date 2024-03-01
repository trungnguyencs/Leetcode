# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        even = odd = 0
        while head:
            if head.val > head.next.val:
                even += 1
            elif head.val < head.next.val:
                odd += 1
            head = head.next.next
        return 'Even' if even > odd else 'Odd' if odd > even else 'Tie'