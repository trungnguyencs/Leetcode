"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        while cur:
            dummy = tmp = Node()
            while cur:
                if cur.left:
                    tmp.next = cur.left
                    tmp = tmp.next
                if cur.right:
                    tmp.next = cur.right
                    tmp = tmp.next
                cur = cur.next
            cur = dummy.next
        return root