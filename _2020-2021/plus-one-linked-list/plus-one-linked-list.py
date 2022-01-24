# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = cur = fisrtNotNine = ListNode(0, head)
        while cur:
            if cur.val != 9: fisrtNotNine = cur
            cur = cur.next
        fisrtNotNine.val += 1
        fisrtNotNine = fisrtNotNine.next
        while fisrtNotNine:
            fisrtNotNine.val = 0
            fisrtNotNine = fisrtNotNine.next
        return dummy if dummy.val == 1 else dummy.next