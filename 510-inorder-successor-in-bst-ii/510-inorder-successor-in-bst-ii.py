"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        cur = node
        if cur.right:
            cur = cur.right
            while cur.left:
                cur = cur.left
            return cur
        while cur and cur.val <= node.val:
            cur = cur.parent        
        return cur