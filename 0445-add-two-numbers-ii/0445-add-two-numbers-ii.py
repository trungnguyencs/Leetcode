# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = self.linkedListToStack(l1)
        stack2 = self.linkedListToStack(l2)
        dummy = ListNode()
        s = 0
        while stack1 or stack2 or s:
            if stack1:
                s += stack1.pop()
            if stack2:
                s += stack2.pop()
            dummy.next = ListNode(s % 10, dummy.next)
            s //= 10
        return dummy.next
        
    def linkedListToStack(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack