# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maxDiff = float('-inf')
        self.preorder(root, root.val, root.val)
        return self.maxDiff
    
    def preorder(self, root, m, M):
        if not root: return
        self.maxDiff = max(self.maxDiff, root.val - m, M - root.val)
        m, M = min(m, root.val), max(M, root.val)
        self.preorder(root.left, m, M)
        self.preorder(root.right, m, M)