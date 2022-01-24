# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head1 = node1 = ListNode()
        head2 = node2 = ListNode()
        node = head
        while node:
            nxt = node.next
            if node.val < x:
                node1.next = node
                node1 = node1.next
            else:
                node2.next= node
                node2 = node2.next
            node.next = None
            node = nxt
        node1.next = head2.next
        return head1.next