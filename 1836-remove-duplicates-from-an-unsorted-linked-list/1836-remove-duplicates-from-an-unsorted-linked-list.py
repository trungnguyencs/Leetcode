# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        counter = Counter()
        cur = head
        while cur:
            counter[cur.val] += 1
            cur = cur.next
        dummy = cur = ListNode(next=head)
        while cur:
            while cur.next and counter[cur.next.val] > 1:
                cur.next = cur.next.next
            cur = cur.next
        return dummy.next