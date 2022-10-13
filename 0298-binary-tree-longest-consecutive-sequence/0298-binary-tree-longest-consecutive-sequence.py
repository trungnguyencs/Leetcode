# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.postOrder(root)
        return self.ans
    
    def postOrder(self, root):
        if not root: return 0
        left, right = self.postOrder(root.left), self.postOrder(root.right)
        ret = 1
        if root.left and root.val + 1 == root.left.val:
            ret = max(ret, 1 + left)
        if root.right and root.val + 1 == root.right.val:
            ret = max(ret, 1 + right)
        self.ans = max(self.ans, ret)
        return ret