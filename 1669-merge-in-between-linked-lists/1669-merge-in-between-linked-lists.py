# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(next=list1)
        cur = dummy
        for _ in range(a):
            cur = cur.next
        prevA = cur
        for _ in range(b - a + 2):
            cur = cur.next
        # connect list1 first half to list2 head
        prevA.next = list2
        while list2.next:
            list2 = list2.next
        # connect list 2 tail to list1 second half
        list2.next = cur
        return dummy.next