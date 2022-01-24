"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self.helper(head)
        return head
    
    def helper(self, head):
        if not head: return None
        prev = Node(-1, next=head)
        cur = head
        while cur:
            if cur.child: #flatten cur.child, then flatten cur.next
                tmp = cur.next
                newHead = self.helper(cur.child)
                cur.next, cur.child.prev, cur.child = cur.child, cur, None
                if tmp:
                    newHead.next = tmp
                    tmp.prev = newHead
                    cur = self.helper(tmp)
            prev, cur = cur, cur.next
        return prev    