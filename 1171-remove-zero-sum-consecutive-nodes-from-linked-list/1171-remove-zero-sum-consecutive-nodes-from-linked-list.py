# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prefixSum = {}
        cur, curSum = dummy, 0
        # first pass is to find the lastest node for each prefix sum
        while cur:
            curSum += cur.val
            prefixSum[curSum] = cur
            cur = cur.next
        cur, curSum = dummy, 0
        # second pass is to skip the middle nodes between cur and its lastest prefix sum
        while cur:
            curSum += cur.val
            cur.next = prefixSum[curSum].next
            cur = cur.next
        return dummy.next