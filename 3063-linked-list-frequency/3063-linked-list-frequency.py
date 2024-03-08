# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        freqHead = None
        dic = {}
        while cur:
            val = cur.val
            if val not in dic:
                dic[val] = ListNode(val=1, next=freqHead)
                freqHead = dic[val]
            else:
                dic[val].val += 1
            cur = cur.next
        return freqHead