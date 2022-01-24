# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = float('-inf')
        self.postOrder(root)
        return self.maxSum
        
    def postOrder(self, root):
        if not root: return 0
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)
        ret = max(root.val, left + root.val, right + root.val)
        self.maxSum = max(self.maxSum, ret, left + right + root.val)
        return ret