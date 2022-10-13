# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        componentCount = 0
        while head:
            if head.val in nums:
                componentCount += 1
                while head.next and head.next.val in nums:
                    head = head.next
            head = head.next
        return componentCount