"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return None
        self.cur = dummy = Node()
        self.inOrder(root)
        dummy.right.left = self.cur
        self.cur.right = dummy.right
        return dummy.right
    
    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        self.cur.right = root
        root.left = self.cur
        self.cur = root
        self.inOrder(root.right)