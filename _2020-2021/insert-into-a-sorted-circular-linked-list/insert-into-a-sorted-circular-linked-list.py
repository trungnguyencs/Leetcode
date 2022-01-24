"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', val: int) -> 'Node':
        if not head:
            node = Node(val)
            node.next = node
            return node 
        cur = head
        while cur.next != head:
            if cur.val < val <= cur.next.val:
                break
            if cur.val > cur.next.val and ((cur.val <= val) or (val <= cur.next.val)):
                break
            cur = cur.next
        cur.next = Node(val, cur.next)
        return head