# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        self.postOrder(root)
        return self.maxSum
        
    def postOrder(self, root):
        if not root: return 0
        left, right = self.postOrder(root.left), self.postOrder(root.right)
        self.maxSum = max(self.maxSum, root.val, root.val + left, root.val + right, root.val + left + right)
        return max(root.val, root.val + left, root.val + right)