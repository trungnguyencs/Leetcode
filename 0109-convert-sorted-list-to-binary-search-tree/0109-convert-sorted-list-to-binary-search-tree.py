# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        if not head.next: return TreeNode(head.val)
        mid = self.findMiddle(head)
        return TreeNode(mid.val, self.sortedListToBST(head), self.sortedListToBST(mid.next))
    
    def findMiddle(self, head):
        prev = None
        fast = slow = head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None
        return slow