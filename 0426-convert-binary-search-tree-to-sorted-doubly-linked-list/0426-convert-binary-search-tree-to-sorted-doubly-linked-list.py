"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        self.dummy = self.cur = TreeNode()
        self.inorder(root)
        #make it circular:
        self.cur.right, self.dummy.right.left = self.dummy.right, self.cur
        return self.dummy.right
        
    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.cur.right, root.left = root, self.cur
        self.cur = self.cur.right #advance link list 1 step
        self.inorder(root.right)