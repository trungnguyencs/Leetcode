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
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            cur = node.right
            while cur.left:
                cur = cur.left
            return cur
        while node.parent:
            if node.parent.val > node.val: break
            node = node.parent
        return node.parent