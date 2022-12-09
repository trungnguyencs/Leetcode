# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        self.inOrder(root, root.val, root.val)
        return self.ans
        
    def inOrder(self, root, minVal, maxVal):
        if not root: return
        self.ans = max(self.ans, root.val - minVal, maxVal - root.val)
        minVal, maxVal = min(minVal, root.val), max(maxVal, root.val)
        self.inOrder(root.left, minVal, maxVal)
        self.inOrder(root.right, minVal, maxVal)