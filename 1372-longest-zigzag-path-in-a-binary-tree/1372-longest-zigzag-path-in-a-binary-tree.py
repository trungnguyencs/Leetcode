# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.helper(root)
        return self.ans - 1
    
    def helper(self, root):
        if not root: return [0, 0]
        left = 1 + self.helper(root.left)[1]
        right = 1 + self.helper(root.right)[0]
        self.ans = max(self.ans, left, right)
        return [left, right]