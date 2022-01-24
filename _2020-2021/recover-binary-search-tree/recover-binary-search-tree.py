# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = self.first = self.second = None
        self.inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        return root
    
    def inOrder(self, cur):
        if not cur: return None
        self.inOrder(cur.left)
        if self.prev and self.prev.val > cur.val:
            if not self.first:
                self.first, self.second = self.prev, cur
            else:
                self.second = cur
                return
        self.prev = cur
        self.inOrder(cur.right)