# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        heap = [[head.val, i] for i, head in enumerate(lists) if head]
        heapify(heap)
        while heap:
            val, i = heappop(heap)
            cur.next = lists[i]
            cur = cur.next
            lists[i] = lists[i].next
            if lists[i]:
                heappush(heap, [lists[i].val, i])
        return dummy.next