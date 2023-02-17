# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.last = float('-inf')
        self.minDiff = float('inf')
        self.inorder(root)
        return self.minDiff
    
    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.minDiff = min(self.minDiff, root.val - self.last)
        self.last = root.val
        self.inorder(root.right)