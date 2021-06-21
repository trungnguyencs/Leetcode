# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.ans = 0
        self.postOrder(root)
        return self.ans
        
    def postOrder(self, root):
        if not root: return 0
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)
        length = 1
        if root.left and root.left.val == root.val + 1: length = max(length, 1 + left)
        if root.right and root.right.val == root.val + 1: length = max(length, 1 + right)
        self.ans = max(self.ans, length)
        return length