# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = []
        totalLength = self.getLength(head)
        sectionLength, r = totalLength//k, totalLength % k
        for _ in range(k):
            dummy = cur = ListNode(next=head)
            for _ in range(sectionLength):
                cur = cur.next
            if r > 0:
                cur = cur.next
                r -= 1
            head = cur.next
            cur.next = None
            ans.append(dummy.next)
        return ans
    
    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length